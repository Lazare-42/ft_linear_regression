import argparse
from graphics import *
from treatData import *

class regressionValues:
    def __init__(self, theta_zero, theta_one, learningRate, iterations):
        self.theta_zero     = theta_zero
        self.theta_one      = theta_one
        self.learningRate   = learningRate 
        self.iterations     = iterations 

def estimatePrice(regressionValues, mileage):
    return regressionValues.theta_zero + regressionValues.theta_one * mileage

def derivativeThetaZero(data, regressionValues):
    result = float(0.0)
    for n in data:
        result += estimatePrice(regressionValues, n[0]) - n[1]
    return result / len(data)

def derivativeThetaOne(data, regressionValues):
    result = float(0.0)
    for n in data:
        result += (estimatePrice(regressionValues, n[0]) - n[1]) * n[0]
    return result / len(data)

def linearRegression(data, regressionValues):
    for iteration in range(regressionValues.iterations):
        regressionValues.theta_zero = regressionValues.theta_zero - regressionValues.learningRate * derivativeThetaZero(data, regressionValues)
        regressionValues.theta_one  = regressionValues.theta_one  - regressionValues.learningRate * derivativeThetaOne(data, regressionValues)
    return regressionValues

def main():

    #parser = argparse.ArgumentParser()
    #parser.add_argument("--iter", type=float, default=2000)
    #parser.add_argument("--thetaZero", type=float, default=0.0)
    #parser.add_argument("--thetaOne", type=float, default=0.0)
    #parser.add_argument("--learningRate", type=float, default=0.0)
    #parser.add_argument("--data", default="./data_realEstate_paris.csv")
    #parser.parse_args()

    theta_zero          = float(0.0)
    theta_one           = float(0.0)
    learningRate        = float(0.01)
    iterations          = 20000

    data                = getData()
    dataSetRange        = getDataSetRange(data)
    data                = normalizeData(data, dataSetRange)
    regVal              = regressionValues(theta_zero, theta_one, learningRate, iterations)
    
    regVal = linearRegression(data, regVal)
    thetas = (regVal.theta_zero, regVal.theta_one)
    
    showOriginalDataPoints((data))
    abline(thetas[1], thetas[0])
    show()

if __name__ == '__main__':
    main()
