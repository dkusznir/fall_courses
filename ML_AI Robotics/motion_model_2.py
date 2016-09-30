#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import math

theta = 0
prev_x = 0
data_set_2 = np.loadtxt('ds0_Odometry.dat')
ground_truth_data = np.loadtxt('ds0_Groundtruth.dat')
gx_val = []
gy_val = []
for key in ground_truth_data:
    gx_val.append(key[1])
    gy_val.append(key[2])
x_values = []
y_values = []
first_loop = True
t_0 = data_set_2[0][0]
t_1 = data_set_2[1][0]
very_first_loop = True

for key in data_set_2:
    init_x = 0
    init_y = 0
    x_values.append(init_x)
    y_values.append(init_y)
    if very_first_loop == True:
        t_0 = key[0]
        very_first_loop = False
        continue
    t_1 = key[0]
    t_d = (t_1 - t_0)
    linear_distance = (key[1]*t_d)
    angular_distance = (key[2]*t_d)
    theta += angular_distance

    if first_loop == True:
        new_x = init_x + (linear_distance*(math.cos(theta)))
        new_y = init_y + (linear_distance*(math.sin(theta)))
        x_values.append(new_x)
        y_values.append(new_y)
        prev_x = new_x
        prev_y = new_y
        t_0 = key[0]
        first_loop = False

    else:
        new_x = prev_x + (linear_distance*(math.cos(theta)))
        new_y = prev_y + (linear_distance*(math.sin(theta)))
        x_values.append(new_x)
        y_values.append(new_y)
        prev_x = new_x
        prev_y = new_y
        t_0 = key[0]

for key in x_values:
    print key

plt.plot(x_values, y_values, 'bs')
plt.hold
plt.plot(gx_val, gy_val, '--')
plt.show()
