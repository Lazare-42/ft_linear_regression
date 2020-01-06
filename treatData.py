import csv
from operator import itemgetter
from graphics import plot

class dataSetRange:
    def __init__(self, max_X, min_X, max_Y, min_Y):
        self.max_X = max_X
        self.min_X = min_X
        self.max_Y = max_Y
        self.min_Y = min_Y

def convertStringToFLoatTuple(data):
    data_sort = []
    for n in data:
        data_sort.append(tuple(map(float, n)))
    return data_sort

def denormalizeOneDataPoint(point, dataSetRange):
    point_X = point[0]
    point_Y = point[1]
    point_Y = (point_Y * (dataSetRange.max_Y - dataSetRange.min_Y)) + dataSetRange.min_Y
    point_X = (point_X * (dataSetRange.max_X - dataSetRange.min_X)) + dataSetRange.min_X
    return (point_X, point_Y)

def normalizeOneDataPoint(point, dataSetRange):
    point_X = point[0]
    point_Y = point[1]
    point_Y = (point_Y - dataSetRange.min_Y) / (dataSetRange.max_Y - dataSetRange.min_Y)
    point_X = (point_X - dataSetRange.min_X) / (dataSetRange.max_X - dataSetRange.min_X)
    return (point_X, point_Y)

def getDataSetRange(data):
    dataRange = dataSetRange((max(data, key=itemgetter(0))[0]), (min(data, key=itemgetter(0))[0]), (max(data, key=itemgetter(1))[1]), (min(data, key=itemgetter(1))[1]))
    return (dataRange)

def normalizeData(data, dataSetRange):
    return [normalizeOneDataPoint(t, dataSetRange) for t in data]

def denormalizeData(data, dataSetRange):
    return [denormalizeOneDataPoint(t, dataSetRange) for t in data]

def getData():
    return convertStringToFLoatTuple(plot(list(csv.reader(open("./data.csv")))))
