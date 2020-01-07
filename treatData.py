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

def denormalizeY(point_Y, dataSetRange):
    point_Y = (point_Y * (dataSetRange.max_Y - dataSetRange.min_Y)) + dataSetRange.min_Y
    return (point_Y)

def denormalizeX(point_X, dataSetRange):
    point_X = (point_X * (dataSetRange.max_X - dataSetRange.min_X)) + dataSetRange.min_X
    return (point_X)

def normalizeY(point_Y, dataSetRange):
    point_Y = (point_Y - dataSetRange.min_Y) / (dataSetRange.max_Y - dataSetRange.min_Y)
    return (point_Y)

def normalizeX(point_X, dataSetRange):
    point_X = (point_X - dataSetRange.min_X) / (dataSetRange.max_X - dataSetRange.min_X)
    return (point_X)

def denormalizeOneDataPoint(pointTuple, dataSetRange):
    return (denormalizeX(pointTuple[0], dataSetRange), (denormalizeY(pointTuple[1], dataSetRange)))

def normalizeOneDataPoint(pointTuple, dataSetRange):
    return (normalizeX(pointTuple[0], dataSetRange), (normalizeY(pointTuple[1], dataSetRange)))

def getDataSetRange(data):
    dataRange = dataSetRange((max(data, key=itemgetter(0))[0]), (min(data, key=itemgetter(0))[0]), (max(data, key=itemgetter(1))[1]), (min(data, key=itemgetter(1))[1]))
    return (dataRange)

def normalizeData(data, dataSetRange):
    return [normalizeOneDataPoint(t, dataSetRange) for t in data]

def denormalizeData(data, dataSetRange):
    return [denormalizeOneDataPoint(t, dataSetRange) for t in data]

def getData(fileName):
    data = plot(list(csv.reader(open(fileName))))
    dataFields = data[0]
    data.pop(0)
    return (dataFields, convertStringToFLoatTuple(data))
