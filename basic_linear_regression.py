import argparse
from graphics import *
from treatData import *
from regression import (linearRegression, regressionValues)

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--iter", type=int, default=20000)
    parser.add_argument("--thetaZero", type=float, default=0.0)
    parser.add_argument("--thetaOne", type=float, default=0.0)
    parser.add_argument("--learningRate", type=float, default=0.01)
    parser.add_argument("--data", default="./data.csv")
    args = parser.parse_args()
    return args

def userLoop(dataFields, data, regVal):
    dataSetRange        = getDataSetRange(data)
    data                = normalizeData(data, dataSetRange)
    valueToEstimateX    = float(input("Input a " + dataFields[0] +
    ", and the program will estimate its corresponding " + dataFields[1] + " : "))

    thetas = linearRegression(data, regVal)

    valueToEstimateY = denormalizeY((normalizeX(valueToEstimateX, dataSetRange) * thetas[1] + thetas[0]), dataSetRange)
    print("For " + str(valueToEstimateX) + dataFields[0] + ", the estimated " + dataFields[1] + " is " + str(valueToEstimateY))
    showEstimatedPoint((valueToEstimateX, valueToEstimateY))
    showOriginalDataPoints(denormalizeData(data, dataSetRange))
    abline(thetas[1], thetas[0], dataSetRange)
    show()


    #data.append((valueToEstimateX, valueToEstimateY))
    #userLoop(dataFields, data, regVal)


def main():
    args                = parse()
    (dataFields, data)  = getData(args.data)
    regVal              = regressionValues(args.thetaZero, args.thetaOne, args.learningRate, args.iter)
    userLoop(dataFields, data, regVal)
    
    #regVal = linearRegression(data, regVal)
    #thetas = (regVal.theta_zero, regVal.theta_one)
    #

if __name__ == '__main__':
    main()
