import argparse
from treatData import *
import csv

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

    dataSetRange            = getDataSetRange(data)
    data                    = normalizeData(data, dataSetRange)

    for iteration in range(regressionValues.iterations):
        tmp_theta_zero = regressionValues.theta_zero - regressionValues.learningRate * derivativeThetaZero(data, regressionValues)
        tmp_theta_one  = regressionValues.theta_one  - regressionValues.learningRate * derivativeThetaOne(data, regressionValues)
    regressionValues.theta_zero = tmp_theta_zero
    regressionValues.theta_one  = tmp_theta_one 

    valueToEstimateY = denormalizeY((normalizeX(45000, dataSetRange) * regressionValues.theta_one + regressionValues.theta_zero), dataSetRange)
    print(valueToEstimateY)
    return (denormalizeY(regressionValues.theta_zero, dataSetRange), denormalizeX(regressionValues.theta_one, dataSetRange))

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--iter", type=int, default=200000)
    parser.add_argument("--learningRate", type=float, default=0.01)
    parser.add_argument("--data", default="./data.csv")
    args = parser.parse_args()
    return args

def main():

    args                    = parse()
    (theta_zero, theta_one) = map(float, list(csv.reader(open("./initialThetas.csv")))[0])
    regVal                  = regressionValues(theta_zero, theta_one, args.learningRate, args.iter)
    (dataFields, data)      = getData(args.data)

    (theta_zero, theta_one) = linearRegression(data, regVal)
    raw                     = open('initialThetas.csv', 'w')
    raw.write(str(theta_zero) + "," + str(theta_one))

if __name__ == '__main__':
    main()
