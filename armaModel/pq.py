import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import acf, pacf


def findp(data):
    """Finds the value for p in arma(p,q) model with acf function

    Arguments:
        data {list} -- data being used
    """
    result = acf(x=birth, unbiased=False, fft=True)

    sampleSize = len(data)
    lag = 0
    for i in result:
        critVal = (1.96)/((sampleSize - lag)**(1/2))
        if abs(i) < critVal:
            return lag
        lag += 0


def findq(data, alpha = 0.5):
    """Finds the value for q in arma(p,q) model with pacf function

    Arguments:
        data {list} -- data being used
    """
    result = pacf(x=birth)

    lag = 0
    for i in result:
        if abs(i) < alpha:
            return lag
        lag += 1


if __name__ == "__main__":
    data = pd.read_csv("testData.csv")
    print(data.head())

    birth = data['Births'].to_list()
    p = findp(birth)
    q = findq(birth)
    print("Value of p is ", str(p))
    print("Value of q is ", str(q))
