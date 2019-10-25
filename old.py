def getMean(data):
    mysum = float(0.0)
    for n in data:
        print(n)
        mysum += n[0] / n[1]
    mysum /= len(data)
    print (mysum)

def getSquaredDeviationSum(data):
    """Cost function / squared error function"""
    result = float(0.0)
    for n in data:
        result += (estimatePrice(n[0]) - n[1]) * (estimatePrice(n[0]) - n[1])
    result /= (2 * len(data))
    return (result)

