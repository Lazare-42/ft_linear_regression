import csv
from operator import itemgetter
from graphics import plot

class dataSetRange:
    def __init__(self, max_Y, min_Y):
        self.max_Y = max_Y
        self.min_Y = min_Y

def convertStringToFLoatTuple(data):
    data_sort = []
    for n in data:
        data_sort.append(tuple(map(float, n)))
    return data_sort

def denormalizeOneDataPoint(point_Y, dataSetRange):
    return ((point_Y * (dataSetRange.max_Y - dataSetRange.min_Y)) + dataSetRange.min_Y)

def normalizeOneDataPoint(point_Y, dataSetRange):
    return ((point_Y - dataSetRange.min_Y) / (dataSetRange.max_Y - dataSetRange.min_Y))

def getDataSetRange(data):
    print((max(data, key=itemgetter(1))[1], min(data, key=itemgetter(1))[1]))
    dataRange = dataSetRange((max(data, key=itemgetter(1))[1]), (min(data, key=itemgetter(1))[1]))
    return (dataRange)

def normalizeData(data, dataSetRange):
    return [(t[0], normalizeOneDataPoint(t[1], dataSetRange)) for t in data]

def denormalizeData(data, dataSetRange):
    return [(t[0], denormalizeOneDataPoint(t[1], dataSetRange)) for t in data]

def getData():
    return convertStringToFLoatTuple(plot(list(csv.reader(open("./data.csv")))))
