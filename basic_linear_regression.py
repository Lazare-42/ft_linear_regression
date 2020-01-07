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

def main():

    args                = parse()
    data                = getData(args.data)
    dataSetRange        = getDataSetRange(data)
    data                = normalizeData(data, dataSetRange)
    regVal              = regressionValues(args.thetaZero, args.thetaOne, args.learningRate, args.iter)
    
    regVal = linearRegression(data, regVal)
    thetas = (regVal.theta_zero, regVal.theta_one)
    print(thetas)
    
    showOriginalDataPoints((data))
    abline(thetas[1], thetas[0])
    show()

if __name__ == '__main__':
    main()
