import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points.iloc[:, 0]
        y = points.iloc[:, 1]
        

def main():
    # Step 1 : Get data
    points = pd.read_csv('data.csv')

    # Step 2 : Define hyperparameters
    learning_rate = 0.0001
    initial_m = 0
    initial_b = 0
    num_iterations = 1000

    # Step 3 : Train our model
    print('Starting gradient descent at b = {0}, m = {1}, error = {2}'.format(
        initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points)))
        
    # [b, m] = gradient_descent(points, initial_b, initial_m, learning_rate, num_iterations)

    # print('Ending gradient descent at b = {1}, m = {2}, error = {3} with {0} iterations'.format(
    #     num_iterations, b, m, compute_error_for_line_given_points(b, m, points)))

if __name__ == '__main__':
    main()
