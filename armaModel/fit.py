import numpy as np
import pylab as py
from scipy.optimize import minimize
from scipy import stats
import pandas as pd
from statistics import stdev

global data

global ydata
global xdata


def fit(p=1, q=1):
    # these vary based on how many parameters you need for your model
    # so like for a ARMA(1,1) you need 4 params

    # set as such:
    # param[0] = c
    #
    # param[1] = gamma
    # param[2] = theta
    # param[3] = standardDev

    initParams = [1] * 4

    # the heavy lifting, need to understand at some point lol
    results = minimize(arma, initParams, method='Nelder-Mead')
    print(results.x)

    estimatedParams = results.x


def arma(params):
    # constant value
    c = params[0]

    # auto-regressive parameter for lag
    gamma = params[1]
    # moving-average parameter for lag
    theta = params[2]

    # standardDeviation param
    sd = params[3]

    # returns random "white noise"
    errorTerm = np.random.normal(0, sd**2)

    # idk about this? lol
    laggederror = 1

    yPred = []
    for i in range(0, len(ydata)-2):
        yPred.append(0)

    for i in range(1, len(ydata)-1):
        # here we are getting a predicted value from previous values
        yPred[i-1] = c + errorTerm + (gamma * ydata[i-1]) + (theta * laggederror)
        # here we calculate the error of that prediction
        laggederror = abs(yPred[i-1] - ydata[i])

    # calculate likelihood
    LL = -np.sum(stats.norm.logpdf(ydata[1:len(ydata)-1], loc=yPred, scale=sd))
    return LL


if __name__ == "__main__":
    data = pd.read_csv("testData.csv")

    ydata = data['Births'].to_list()

    fit()
