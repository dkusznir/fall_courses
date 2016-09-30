#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import math

theta = 90
prev_x = 0
data_set = [[0.5,0,1], [0,-90,1], [0.5,0,1], [0,90,1], [0.5,0,1]]
data_set_2 = np.loadtxt('ds0_Odometry.dat')
x_values = []
y_values = []
first_loop = True

for key in data_set:
    init_x = 0
    init_y = 0
    x_values.append(init_x)
    y_values.append(init_y)
    linear_distance = (key[0]*key[2])
    angular_distance = (key[1]*key[2])
    theta += angular_distance

    if first_loop == True:
        #if angular_distance == 0:
        new_x = init_x + (linear_distance*(math.cos(math.radians(theta))))
        new_y = init_y + (linear_distance*(math.sin(math.radians(theta))))
        #new_x = init_x + (linear_distance*float(math.cos(theta))
        #new_y = init_y + (linear_distance*float(math.sin(theta))
        x_values.append(new_x)
        y_values.append(new_y)
        prev_x = new_x
        prev_y = new_y
        first_loop = False

    else:
        #if angular_distance == 0:
        new_x = prev_x + (linear_distance*(math.cos(math.radians(theta))))
        new_y = prev_y + (linear_distance*(math.sin(math.radians(theta))))
        #new_x = prev_x + (linear_distance*float(math.cos(theta))
        #new_y = prev_y + (linear_distance*float(math.sin(theta))
        if new_x == prev_x and new_y == prev_y:
            continue
        x_values.append(new_x)
        y_values.append(new_y)
        prev_x = new_x
        prev_y = new_y

def calculate_new_coord(x,y,w):
    new_x = x + (linear_distance*(math.cos(math.radians(w))))
    new_y = y + (linear_distance*(math.sin(math.radians(w))))

def calculate_displacement(v, a, t):
    if a == 0:
        theta = 90
        new_x = init_x + ((key[0]*key[2])*math.cos(theta))
        new_y = init_y + ((key[0]*key[2])*math.sin(theta))

points = plt.plot(x_values, y_values, 'bs')
plt.axis([-2, 2, -2, 2])
#plt.setp(points, color='b', linewidth=2.0)
#plt.plot(points, color='b', linewidth=2.0)
plt.show()
