#!usr/bin/env python
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as patches

####Set up grid####
fig, ax = plt.subplots()
#Create nodes and append to an array
x_vals = []
y_vals = []
for x in range(-2,6):
    for y in range(-6,7):
        x_vals.append(x)
        y_vals.append(y)

#Load landmarks and assign values to grid
landmarks = np.loadtxt('ds1_Landmark_Groundtruth.dat')
lms_x_y = []
for key in landmarks:
    lms_x_y.append([key[1], key[2]])

def obstacles(x, y):
    o_x = x - 0.5
    o_y = y - 0.5
    obst = []
    obst.append([o_x, o_y])
    print obst

#Cast each landmark to int
for key in lms_x_y:
    max_x = math.ceil(key[0])
    max_y = math.ceil(key[1])
    min_x = max_x - 1
    min_y = max_y - 1

    obstacles(max_x, max_y)

    landmark_points = [max_x, min_x, max_y, min_y]
    ax.add_patch(patches.Rectangle((min_x, min_y), 1, 1, fill=True))
    #ax.plot([max_x, min_x, max_x, min_x], [max_y, min_y, min_y, max_y], 'rs')
    ax.hold

def start_cell(x, y):
    start_x = math.ceil(x) - 0.5
    start_y = math.ceil(y) - 0.5
    return start_x, start_y

def get_neighbors(cell):
    dirs = [[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1]]
    nbrs = []

    for i in dirs:
        nbrs.append(((cell[0] + i[0]), (cell[1] + i[1])))
    return nbrs

x, y = start_cell(2, 2)
start_c = [x, y]
neighbors = get_neighbors(start_c)
for key in neighbors:
    ax.plot(key[0], key[1], 'ro')
ax.plot(start_c[0], start_c[1], 'rs')
ax.hold


#Set up grid
loc = ticker.MultipleLocator(base=1.0)
ax.xaxis.set_major_locator(loc)
ax.yaxis.set_major_locator(loc)
ax.grid(which='major', axis='both')
plt.xticks(np.arange(min(x_vals), max(x_vals)+1, 1.0))
plt.yticks(np.arange(min(y_vals), max(y_vals)+1, 1.0))
plt.show()

def heuristic(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)
