#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import math
from motion_model_A import calculate_values
from measurement_model import calculate_measurement_model

#Measurement model - prints x, y and theta values for robot position.
meas_x, meas_y, meas_theta = calculate_measurement_model()
#Data set from hw0.
data_set_1 = [[1,0.5,0], [1,0,-90], [1,0.5,0], [1,0,90], [1,0.5,0]]

#Create 2 subplots to show answers for Part A - Problems 2 & 3
fig = plt.figure()
plt1 = fig.add_subplot(221)
plt1.set_title("Motion Model: Part A, Problem 2")
plt1.axis([-0.5, 1, -1, 2])
plt2 = fig.add_subplot(222)
plt2.set_title("Motion Model: DS0")
plt3 = fig.add_subplot(223)
plt3.set_title("Measurement Model: DS0")

#Upload Groundtruth data file and parse to extract x, y, theta values into separate arrays. Add these values to plt2.
ground_truth_data = np.loadtxt('ds0_Groundtruth.dat')
gx_val = []
gy_val = []
gw_val = []
for key in ground_truth_data:
    gx_val.append(key[1])
    gy_val.append(key[2])
    gw_val.append(key[3])
plt2.plot(gx_val, gy_val, '-')
plt2.hold

#Calculate and plot Part A - Problem 2
problem_2_calc = calculate_values(data_set_1, 0, 0, 90)
plt1.plot(problem_2_calc[0], problem_2_calc[1], 'bs')

#Calculate and plot Part A - Problem 3
problem_3_calc = calculate_values('ds0_Odometry.dat', gx_val[0], gy_val[0], gw_val[0])
plt2.plot(problem_3_calc[0], problem_3_calc[1], 'bs')

plt3.plot(meas_x, meas_y, '-')
#Show both subplots
plt.show()
