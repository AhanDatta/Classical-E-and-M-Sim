#This file plots the results of the simulation
import matplotlib.pyplot as plt
import numpy as np
from Particle_Class import Particle
import Simulator

#Takes a list of lists lst and returns a list of the ith element of each sublist
def Extract(lst, i):
    answer = []
    for sub in lst:
        answer.append(sub[i])
    return answer

#Defines a dictionary to color the subplots
color_dict = {
    0: "r",
    1: "g",
    2: "b"
}

#Defines a dictionary to label the direction of each plot 
dir_dict = {
    0: "x",
    1: "y",
    2: "z"
}

#Getting the plotting lists from the simulation
time_axis = np.arange(0, Simulator.end_time + Simulator.dt, Simulator.dt)
positions = Simulator.position_in_time
velocities = Simulator.velocity_in_time
accelerations = Simulator.accel_in_time

#Fixes length of lists to ensure plotting works
if len(time_axis) > len(positions[0]):
    for i in range(len(positions)):
        positions[i].append(positions[i][-1])
        velocities[i].append(velocities[i][-1])
        accelerations[i].append(accelerations[i][-1])
elif len(time_axis) < len(positions[0]):
    time_axis = [0] + time_axis

#Creating position vs time and velocity vs time plots for each particle in each direction of motion
for i in range(len(positions)):
    #Creates a figure and axes with a certain layout
    fig, axd = plt.subplot_mosaic([['0', '1'],
                                ['2', '2']],
                                layout="constrained")
    
    fig.suptitle("Particle " + str(i+1) + " Position")

    #Puts the position wrt a axis on each of the axes
    for k, ax in axd.items():
        ax.plot(time_axis, Extract(positions[i], int(k)), color_dict[int(k)])
        ax.set_xlabel("Time [s]")
        ax.set_ylabel(dir_dict[int(k)] + " position [m]")

for i in range(len(velocities)):
    #Creates a figure and axes with a certain layout
    fig, axd = plt.subplot_mosaic([['0', '1'],
                                ['2', '2']],
                                layout="constrained")
    
    fig.suptitle("Particle " + str(i+1) + " Velocity")

    #Puts the position wrt a axis on each of the axes
    for k, ax in axd.items():
        ax.plot(time_axis, Extract(velocities[i], int(k)), color_dict[int(k)])
        ax.set_xlabel("Time [s]")
        ax.set_ylabel(dir_dict[int(k)] + " velocity [m/s]")

for i in range(len(accelerations)):
    #Creates a figure and axes with a certain layout
    fig, axd = plt.subplot_mosaic([['0', '1'],
                                ['2', '2']],
                                layout="constrained")
    
    fig.suptitle("Particle " + str(i+1) + " Acceleration")

    #Puts the position wrt a axis on each of the axes
    for k, ax in axd.items():
        ax.plot(time_axis, Extract(accelerations[i], int(k)), color_dict[int(k)])
        ax.set_xlabel("Time [s]")
        ax.set_ylabel(dir_dict[int(k)] + " acceleration [m/s^2]")

plt.show()