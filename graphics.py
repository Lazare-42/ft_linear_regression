import matplotlib.pyplot as plt
import numpy as np

def normalizeX(point_X, dataSetRange):
    point_X = (point_X - dataSetRange.min_X) / (dataSetRange.max_X - dataSetRange.min_X)
    return (point_X)

def denormalizeY(point_Y, dataSetRange):
    point_Y = (point_Y * (dataSetRange.max_Y - dataSetRange.min_Y)) + dataSetRange.min_Y
    return (point_Y)

def abline(normalizedSlope, normalizedIntercept, dataSetRange):
    """Plot a line from normalizedSlope and normalizedIntercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    normalizedX = [normalizeX(x, dataSetRange) for x in x_vals]
    y_vals = [denormalizeY(normalizedIntercept + normalizedSlope * x, dataSetRange) for x in normalizedX]
    plt.plot(x_vals, y_vals, '--')

def showOriginalDataPoints(data):
    x_val = [x[0] for x in data]
    y_val = [x[1] for x in data]
    plt.scatter(x_val, y_val) 

def showEstimatedPoint(point):
    plt.plot(point[0], point[1], marker='o', markersize=5, color="red")

def plot(data):
    plt.xlabel(data[0][0])
    plt.ylabel(data[0][1])
    return (data)

def show():
    plt.title("ft_linear_regression")
    plt.show()

