import matplotlib.pyplot as plt
import numpy as np

def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
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
    plt.draw()
    plt.pause(0.1)

