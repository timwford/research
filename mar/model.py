import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import minimize
from scipy import stats


class Var:

    def __init__(self, n, data):
        self.vectorSize = n
        self.matrixSize = n * n

        self.data = data

        self.constants = [1] * self.vectorSize
        self.ARparam = [1] * self.matrixSize
        self.MAparam = [1] * self.matrixSize
        self.errors = [0] * self.vectorSize
        self.feedback = [1] * self.matrixSize

    def __str__(self):
        response = "Var on size {n} vector".format(n=self.vectorSize) + "\n"
        response += "Constants: "
        response += str(self.constants) + "\n"
        response += "AR Parameters: "
        response += str(self.ARparam) + "\n"
        response += "MA Parameters: "
        response += str(self.MAparam) + "\n"
        response += "Error Terms: "
        response += str(self.errors) + "\n"
        response += "Feedback Terms: "
        response += str(self.feedback) + "\n"
        return response

    def stackParameters(self):
        return self.constants + self.ARparam + self.MAparam + self.errors + self.feedback

    def unstackParameters(self, params):
        # constants:
        c = params[0:self.vectorSize]
        offset = self.vectorSize

        self.constants = c

        # AR params:
        offsetEnd = offset + self.matrixSize
        ar = params[offset:offsetEnd]
        offset += self.matrixSize

        self.ARparam = ar

        # MA params:
        offsetEnd = offset + self.matrixSize
        ma = params[offset:offsetEnd]
        offset += self.matrixSize

        self.MAparam = ma

        # Error params:
        offsetEnd = offset + self.vectorSize
        e = params[offset:offsetEnd]
        offset += self.vectorSize

        self.errors = e

        # Feedback params:
        offsetEnd = offset + self.matrixSize
        f = params[offset:offsetEnd]

        self.feedback = f

    def model(self, params, predictions=False):
        # unpack Parameters
        # constants:
        c = params[0:self.vectorSize]
        c = np.reshape(c, (self.vectorSize, 1))
        offset = self.vectorSize

        # AR params:
        offsetEnd = offset + self.matrixSize
        ar = params[offset:offsetEnd]
        ar = np.reshape(ar, (self.vectorSize, self.vectorSize))
        offset += self.matrixSize

        # MA params:
        offsetEnd = offset + self.matrixSize
        ma = params[offset:offsetEnd]
        ma = np.reshape(ma, (self.vectorSize, self.vectorSize))
        offset += self.matrixSize

        # Error params:
        offsetEnd = offset + self.vectorSize
        e = params[offset:offsetEnd]
        e = np.reshape(e, (self.vectorSize, 1))
        offset += self.vectorSize

        # Feedback params:
        offsetEnd = offset + self.matrixSize
        f = params[offset:offsetEnd]
        f = np.reshape(f, (self.vectorSize, self.vectorSize))
        offset += self.matrixSize

        # create matrices for model:
        a_0 = f.dot(c)
        A_1 = f.dot(ar)
        B_1 = f.dot(ma)
        u_t = f.dot(e)

        # The Model:
        # matrix to hold predicted values
        predict = np.zeros((self.vectorSize, len(self.data)))

        # run the Model
        for i in range(0, len(self.data)):
            #
            # y = B_inverse * constant + B_inverse * AR_params + B_inverse * MA_params + B_inverse * errors
            # V       M          V           M           M          M            M           M         V
            #
            # y =           a0         +          A1           +           B1          +        ut

            if i == 0:
                temp = np.reshape(self.data[0], (self.vectorSize, 1))
            else:
                # TODO: error terms are not doing anything
                temp = a_0 + A_1.dot(np.reshape(self.data[i-1], (self.vectorSize, 1))) + u_t

            predict[:, i] = temp[:, 0]

        # return the predicted values from model
        if predictions:
            return predict

        # return likelihood for minimize function
        # TODO: might need to add scale in again, refer to
        dataMatrix = np.reshape(self.data, (self.vectorSize, len(self.data)))
        LL = -np.sum(stats.norm.logpdf(dataMatrix.flatten(), loc=predict.flatten()))

        return LL

    def fit(self, p=1, q=1):
        results = minimize(self.model, self.stackParameters(), method='Nelder-Mead')
        self.unstackParameters(results.x)
        # return = results.x


if __name__ == "__main__":
    # get data
    data = [
        [1, 1],
        [2, 3],
        [2, 4],
        [4, 1]
    ]

    # create a var model
    m = Var(2, data)
    m.fit()
    print(m)

    # print("\n\n")
    # m.model(m.stackParameters())
