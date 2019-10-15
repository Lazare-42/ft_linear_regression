import csv
import matplotlib.pyplot as plt

theta_zero = float(50 * 600) * (-1)
theta_one  = float(0)
precision  = float(0.1)

def showOriginalDataPoints(data):
    x_val = [x[0] for x in data]
    y_val = [x[1] for x in data]
    plt.scatter(x_val, y_val) 

def estimatePrice(mileage):
    return theta_zero + theta_one * mileage

def getSquaredDeviationSum(data):
    """Cost function / squared error function"""
    result = float(0.0)
    for n in data:
        result += (estimatePrice(n[0]) - n[1]) * (estimatePrice(n[0]) - n[1])
    result /= (2 * len(data))
    return (result)

def getMeanPerSquareFoot(data):
    mysum = float(0.0)
    for n in data:
        mysum += n[0] / n[1]
    mysum /= len(data)
    print (mysum)



#def getResult(data):
    

if __name__ == '__main__':
    data = list(csv.reader(open("./data_realEstate_paris.csv")))
    data_categories = data[0]
    data.pop(0)
    data_sort = []
    i = 0
    for n in data:
        data_sort.append(tuple(map(float, n)))
        i += 1

    getMeanPerSquareFoot(data_sort)
    #data_set = []
    #for s in range(1200):
    #    data_set.append(tuple([theta_zero, getSquaredDeviationSum(data_sort)]))
    #    theta_zero += 50

    #x_val = [x[0] for x in data_set]
    #y_val = [x[1] for x in data_set]
    ##plt.plot(x_val, y_val)
    #plt.xlabel(data_categories[0])
    #plt.ylabel(data_categories[1])
    #showOriginalDataPoints(data_sort)
    #plt.show()
