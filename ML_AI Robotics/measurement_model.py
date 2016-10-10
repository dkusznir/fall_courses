#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import math

#Load data files and set them equal to appropriate variables.
barcode_dt = np.loadtxt('ds0_Barcodes.dat')
landmarkgt_dt = np.loadtxt('ds0_Landmark_Groundtruth.dat')
measurement_dt = np.loadtxt('ds0_Measurement.dat')
groundmark_dt = np.loadtxt('ds0_Groundtruth.dat')

#Create new barcodes variable and append only values 5-20 from barcodes data file. This is to account for the 5 data items that we're going to ignore.
barcodes = []
for key in barcode_dt[5:]:
    barcodes.append(key[1])

#Replace Subject values with barcode values. This will make it it easier to iterate and find appropriate matches for the x/y coordinates.
for i,j in zip(landmarkgt_dt, barcodes):
    i[0] = j

#Grab theta values from ds0_Groundtruth.dat and append them to a theta array.
theta = []
for key in groundmark_dt:
    theta.append([key[3]])
    if len(theta) == 6443:
        break

#Create empty arrays for landmark x & y, robot x & y, radius and bearing values
x_lm = []
y_lm = []
r = []
bearing = []
x_r = []
y_r = []
theta_r = []

#Create function to calculate robot position/measurement model.
def calculate_measurement_model():
    #Iterate over measurement data.
    for key in measurement_dt:
        subject = key[1]
        #Ignore data from other robots in the space.
        if subject == 5 or subject == 14 or subject == 41 or subject == 32 or subject == 23:
            continue
        #Additional loop to check landmark data if the subject/barcode key from measurement data equals a key in landmark data. If so, get x and y values and append them to the appropriate arrays.
        for key in landmarkgt_dt:
            if subject == key[0]:
                x_lm.append(key[1])
                y_lm.append(key[2])
        #Grab radius and bearing values.
        r.append(key[2])
        bearing.append(key[3])

    #Loop over each of the landmark, radius and bearing arrays. Calculate appropriate x, y, theta values for the robot and append to the x_r, y_r, theta_r arrays.
    i = 0
    while i < len(x_lm):
        x = x_lm[i] - (r[i]*math.cos(theta[i]+bearing[i]))
        y = y_lm[i] - (r[i]*math.sin(theta[i]+bearing[i]))
        robot_theta = math.atan(((y_lm[i] - y) / (x_lm[i] - x)))
        x_r.append(x)
        y_r.append(y)
        theta_r.append(robot_theta)
        i += 1
    return x_r, y_r, theta_r

'''
def return_x():
    return x_r
def return_y():
    return y_r
def return_theta():
    return theta_r

calculate_measurement_model()
x_test = return_x()
y_test = return_y()

test, test2, test3 = calculate_measurement_model()
plt.plot(test, test2, '-')
plt.show()
'''
