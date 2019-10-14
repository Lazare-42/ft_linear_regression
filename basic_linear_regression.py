import csv
import matplotlib.pyplot as plt

#def estimatePrice(list_array):
#    float theta = 0
#    for f in list_array:
#        theta += 
    

if __name__ == '__main__':
    data = list(csv.reader(open("./data.csv")))
    data_categories = data[0]
    data.pop(0)
    data_sort = []
    for n in data:
        data_sort.append(tuple(map(int, n)))
    x_val = [x[0] for x in data_sort]
    y_val = [x[1] for x in data_sort]
    plt.xlabel(data_categories[0])
    plt.ylabel(data_categories[1])
    plt.plot(x_val, y_val)
    plt.show()
