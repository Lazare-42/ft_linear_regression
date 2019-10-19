import csv
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

theta_zero      = float(0.0)
theta_one       = float(0.0)
learningRate    = float(0.01)
max_Y           = float(0.0)
min_Y           = float(0.0)
iterations      = 20000

def showOriginalDataPoints(data):
    x_val = [x[0] for x in data]
    y_val = [x[1] for x in data]
    plt.scatter(x_val, y_val) 

def estimatePrice(mileage):
    global theta_zero
    global theta_one
    return theta_zero + theta_one * mileage

def getSquaredDeviationSum(data):
    """Cost function / squared error function"""
    result = float(0.0)
    for n in data:
        result += (estimatePrice(n[0]) - n[1]) * (estimatePrice(n[0]) - n[1])
    result /= (2 * len(data))
    return (result)

def derivativeThetaZero(data):
    result = float(0.0)
    for n in data:
        result += estimatePrice(n[0]) - n[1]
    return (result / len(data))

def derivativeThetaOne(data):
    result = float(0.0)
    for n in data:
        result += (estimatePrice(n[0]) - n[1]) * n[1]
    return (result / len(data))

def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')




def linearRegression(data):
    global theta_zero
    global theta_one
    for iteration in range(iterations):
        theta_zero = theta_zero - learningRate * derivativeThetaZero(data)
        theta_one  = theta_one  - learningRate * derivativeThetaOne(data)
    abline(theta_one, theta_zero)

def updateTheta(theta_zero):
    theta_zero = theta_zero - learningRate

def getMean(data):
    mysum = float(0.0)
    for n in data:
        mysum += n[0] / n[1]
    mysum /= len(data)
    print (mysum)

def convertStringToFLoatTuple(data):
    data_sort = []
    for n in data:
        data_sort.append(tuple(map(float, n)))
    return data_sort

def normalizeData(data):
    max_Y = max(data, key=itemgetter(1))[1]
    min_Y = min(data, key=itemgetter(1))[1]
    return [(t[0], (t[1] - min_Y) / (max_Y - min_Y)) for t in data]

def denormalizeData(data):
    print (max_Y)
    print (min_Y)
    return [(t[0], float((t[1] * (max_Y - min_Y)) + min_Y)) for t in data]


if __name__ == '__main__':
    data = list(csv.reader(open("./data_realEstate_paris.csv")))
    data_categories = data[0]
    data.pop(0)
    data = normalizeData(convertStringToFLoatTuple(data))

    data_set = []
    for s in range(1200):
        data_set.append(tuple([theta_zero, getSquaredDeviationSum(data)]))
        theta_zero += 50
    squaredDev = getSquaredDeviationSum(data)

    
    x_val = [x[0] for x in data_set]
    y_val = [x[1] for x in data_set]
    #plt.plot(x_val, y_val)
    showOriginalDataPoints(data)
    plt.xlabel(data_categories[0])
    plt.ylabel(data_categories[1])
    linearRegression(data)
    plt.show()
