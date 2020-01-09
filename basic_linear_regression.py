import argparse
from graphics import *
from treatData import *
from regression import (linearRegression, regressionValues)

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="./data.csv")
    args = parser.parse_args()
    return args

def userLoop(dataFields, data, theta_zero, theta_one):

    dataSetRange            = getDataSetRange(data)
    valueToEstimateX    = float(input("Input a " + dataFields[0] +
    ", and the program will estimate its corresponding " + dataFields[1] + " : "))
    valueToEstimateY = denormalizeY((normalizeX(valueToEstimateX , dataSetRange) * theta_one + theta_zero), dataSetRange)
    print("For " + str(valueToEstimateX) + dataFields[0] + ", the estimated " + dataFields[1] + " is " + str(valueToEstimateY))

    showEstimatedPoint((valueToEstimateX, valueToEstimateY))
    showOriginalDataPoints(data)
    abline(theta_one, theta_zero, dataSetRange)
    show()
    userLoop(dataFields, data, theta_zero, theta_one)

def main():
    args                = parse()
    (dataFields, data)  = getData(args.data)
    plot(data)
    (theta_zero, theta_one) = map(float, list(csv.reader(open("./initialThetas.csv")))[0])
    userLoop(dataFields, data, theta_zero, theta_one)

if __name__ == '__main__':
    main()
