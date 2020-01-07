class regressionValues:
    def __init__(self, theta_zero, theta_one, learningRate, iterations):
        self.theta_zero     = theta_zero
        self.theta_one      = theta_one
        self.learningRate   = learningRate 
        self.iterations     = iterations 

def estimatePrice(regressionValues, mileage):
    return regressionValues.theta_zero + regressionValues.theta_one * mileage

def derivativeThetaZero(data, regressionValues):
    result = float(0.0)
    for n in data:
        result += estimatePrice(regressionValues, n[0]) - n[1]
    return result / len(data)

def derivativeThetaOne(data, regressionValues):
    result = float(0.0)
    for n in data:
        result += (estimatePrice(regressionValues, n[0]) - n[1]) * n[0]
    return result / len(data)

def linearRegression(data, regressionValues):
    for iteration in range(regressionValues.iterations):
        regressionValues.theta_zero = regressionValues.theta_zero - regressionValues.learningRate * derivativeThetaZero(data, regressionValues)
        regressionValues.theta_one  = regressionValues.theta_one  - regressionValues.learningRate * derivativeThetaOne(data, regressionValues)
    return regressionValues

