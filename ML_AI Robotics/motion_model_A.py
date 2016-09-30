#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import math

#If the data file is not .dat, simply convert theta from degrees to radians
#If the data file is .dat, utilize np to load the file.
#Return the file.
def load_data(input_file):
    if '.dat' not in input_file:
        for key in input_file:
            key[2] = math.radians(key[2])
    else:
        input_file = np.loadtxt(input_file)
    return input_file

#Peform calculations to determine position (motion model)
#Parameters: file(data with time, linear velocity and angular velocity)
#Parameters cont'd: x = user's desired initial x, y = user's desired initial y, w = user's desired initial theta.
def calculate_values(desired_file, x, y, w):
    #Call load_data function on desired_file and set equal to my_data
    my_data = load_data(desired_file)

    #Set t_0 and t_1 equal to first and second time values
    t_0 = my_data[0][0]
    t_1 = my_data[1][0]

    #If the file is not .dat (problem in part A, number 2), set t_0 = and t_1 = first value. Time increased at a constant value (1s) for this data set.
    theta = w
    if '.dat' not in desired_file:
        t_0 = 0
        t_1 = my_data[0]
        theta = math.radians(w)

    #Create local variables for initial x & y. Create array for final x and y values and append the initial values to these arrays.
    x_initial = x
    y_initial = y
    x_values = [x_initial]
    y_values = [y_initial]

    #Set this boolean equal to True - this is for the Odometry data set. We want to skip the first set of values in order to have t_0 and t_1 values.
    skip_first_dp = True

    #Loop through data set my_data
    for key in my_data:
        #Skip first data point if data set is .dat (Odometry data). Set the boolean skip_first_dp to False so the rest of the values are processed properly.
        if skip_first_dp == True and '.dat' in desired_file:
            skip_first_dp = False
            continue
        #If the data is not in .dat format (sample set of 5 values from Part A Problem 2) set t_0 equal to 0. Since time increases at a constant rate (t=1), we want to make sure that when we subtract t_1 from t_0, we get a value of 1.
        elif '.dat' not in desired_file:
            t_0 = 0
        #Set t_1 equal to time value of data set data_set_2[i][0]
        #Subtract t_1 from previous time value data_set_2[i-1][0]
        t_1 = key[0]
        t_d = (t_1 - t_0)

        #Grab linear velocity from data_set_2[i][1]
        #Grab angular velocity from data_set_2[i][2]
        #Add/subtract radians/angular distance to/from theta
        linear_distance = (key[1]*t_d)
        angular_distance = (key[2]*t_d)
        theta += angular_distance

        #Set new x and y values accordingly.
        new_x = x_initial + (linear_distance*(math.cos(theta)))
        new_y = y_initial + (linear_distance*(math.sin(theta)))
        #Append new x and y values to x_values and y_values arrays.
        x_values.append(new_x)
        y_values.append(new_y)
        #Set current x and y equal to new x and y for next iteration.
        x_initial = new_x
        y_initial = new_y
        #Set t_0 (t-1) equal to current time (t_1) for next iteration.
        t_0 = key[0]
    #Return an array of x and y values when completed.
    return x_values, y_values
