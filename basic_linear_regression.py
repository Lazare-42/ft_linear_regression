import argparse
from graphics import *
from treatData import *

class regressionValues:
    def __init__(self, theta_zero, theta_one, learningRate, iterations):
        self.theta_zero     = theta_zero
        self.theta_one      = theta_one
        self.learningRate   = learningRate 
        self.iterations     = iterations 

def estimatePrice(mileage, regressionValues):
    return regressionValues.theta_zero + regressionValues.theta_one * mileage

def derivativeThetaZero(data, regressionValues):
    result = float(0.0)
    for n in data:
        result += estimatePrice(n[0], regressionValues) - n[1]
    return (result / len(data))

def derivativeThetaOne(data, regressionValues):
    result = float(0.0)
    for n in data:
        result += (estimatePrice(n[0], regressionValues) - n[1]) * n[1]
    return (result / len(data))

def linearRegression(data, regressionValues):
    for iteration in range(regressionValues.iterations):
        regressionValues.theta_zero = regressionValues.theta_zero - regressionValues.learningRate * derivativeThetaZero(data, regressionValues)
        regressionValues.theta_one  = regressionValues.theta_one  - regressionValues.learningRate * derivativeThetaOne(data, regressionValues)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--iter", type=float, default=2000)
    parser.add_argument("--thetaZero", type=float, default=0.0)
    parser.add_argument("--thetaOne", type=float, default=0.0)
    parser.add_argument("--learningRate", type=float, default=0.0)
    parser.add_argument("--data", default="./data.csv")
    parser.parse_args()
    theta_zero          = float(0.0)
    theta_one           = float(0.0)
    learningRate        = float(0.0)
    iterations          = 2000

    print (theta_zero, theta_zero, learningRate, iterations)
    #data                = getData()
    #dataSetRange        = getDataSetRange(data)
    #data                = normalizeData(data, dataSetRange)
    #regVal              = regressionValues(theta_zero, theta_one, learningRate, iterations)

    #linearRegression(data, regVal)
    #showOriginalDataPoints(denormalizeData(data, dataSetRange))
    #print(denormalizeOneDataPoint(regVal.theta_zero, dataSetRange), denormalizeOneDataPoint(regVal.theta_one, dataSetRange))
    #abline(denormalizeOneDataPoint(regVal.theta_one, dataSetRange), denormalizeOneDataPoint(regVal.theta_zero, dataSetRange))
    #show()

if __name__ == '__main__':
    main()
