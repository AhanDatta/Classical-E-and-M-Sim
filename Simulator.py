#This is the simulation file
import math
from copy import deepcopy
import numpy as np
from Particle_Class import Particle
import User_Input

#Useful electromagnetic constants
EPSILON_0 = 8.854e-12
MU_0 = 4e-7 * math.pi
K = 1/(4 * math.pi * EPSILON_0)

#Timestep Constant
dt = 2e-5

#Ending time for the simulation from user input
end_time = User_Input.end_time

#List of particles in the simulation from user input
particles = User_Input.particles

#Creating lists which track position and velocity for each particle
position_in_time = []
velocity_in_time = []
for i in range(len(particles)):
    position_in_time.append([])
    velocity_in_time.append([])

#Using Runge-Kutta and classical electrodynamics, we simulate the motion of the particles over a given time interval
current_time = 0
while current_time < end_time:
    #Tracks position and velocity updates that need to be made for all particles
    delta_x = []
    delta_v = []

    #Iterates through all particles in simulation
    for i, particle_i in enumerate(particles):
        #Boolean for if particle i is colliding at this point in time
        is_colliding = False

        #Sums the contribution to the magnetic and electric fields of each particle in the simulation
        e_field = np.array([0.,0.,0.])
        B_field = np.array([0.,0.,0.])
        for j, particle_j in enumerate(particles):
            #skips calculations on itself
            if i == j:
                continue
            
            #Gets the current r vector
            r = particle_i.position - particle_j.position

            #Gets the previous 2 r vectors if two cycles have passed
            if current_time > dt:
                r_0 = position_in_time[i][-1] - position_in_time[j][-1]
                r_00 = position_in_time[i][-2] - position_in_time[j][-2]
                #Checks for collision by seeing if the angle between two consecutive r vectors is greater than pi/2, and if the two last vectors are in the same direction, and if so, skips the field calculations
                if np.dot(r_0,r) < 0 and np.dot(r_0, r_00) > 0:
                    is_colliding = True
                    continue

            #Adds to the sum of each field if the particles aren't colliding
            e_field += particle_j.e_field(r)
            B_field += particle_j.B_field(r)

        #If the particle is colliding, uses conservation of momentum and energy to find new velocity (assumes perfect bounce backward)
        if is_colliding:
            delta_v.append(-2 * particle_i.velocity)
            delta_x.append(delta_v[-1] * 10*dt)
            continue
            
        #Finds the net acceleration on a particle using F = ma, F_e = qE = kq(E/k), and F_B = qv x B, so a = (q/m) (E + v x B)
        acceleration = (particle_i.charge/particle_i.mass) * (K * e_field + (MU_0/(4 * math.pi)) * np.cross(particle_i.velocity, B_field))
        
        #Tracks position and velocity updates, using the average of the old and new velocities to update the position
        delta_v.append(acceleration * dt)
        delta_x.append((2*particle_i.velocity + delta_v[-1])/2 * dt)

    #Logs the state of each particle
    for i in range(len(particles)):
        position_in_time[i].append(deepcopy(particles[i].position))
        velocity_in_time[i].append(deepcopy(particles[i].velocity[:]))

    #Updates the state of each particle
    for i in range(len(particles)):
        particles[i].position += delta_x[i]
        particles[i].velocity += delta_v[i]
    #Advances the simulation by one time step
    current_time += dt