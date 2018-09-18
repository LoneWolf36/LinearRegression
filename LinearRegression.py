import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

data =  pd.read_csv('ex1data1.txt', header =  None)
X, y = data.iloc[:, 0], data.iloc[:, 1]

X = X[:, np.newaxis]
y = y[:, np.newaxis]

theta = np.zeros([2, 1])
ones = np.ones([y.size, 1])
X = np.hstack((ones, X))

# Cost = 1/2m Summation i = 1 to m ( h - y )
# h = Theta1 * x + Theta0
def computeCost(X, y, theta):
    m = y.size
    J = 0
    h = X.dot(theta)
    J = 1/(2*m) * np.sum(np.square(h - y))
    return J

# Gradient Descent = Theta - alpha/m Summation i = 1 to m ( h - y )
# h = Theta1 * x + Theta0
    # d/d(theta) J(Theta0, Theta1) = Multiply with transpose
def gradientDescent(X, y, theta):
    m = y.size
    iterations = 1500
    alpha = 0.01
    for iter in range(iterations):
        h = X.dot(theta)
        theta = theta - alpha*(1/m)*(X.T.dot(h - y))




J = computeCost(X, y, theta)
print(J)

#plt.scatter(X, y)
#plt.xlabel('Population in cities')
#plt.ylabel('Profit')
#plt.show()