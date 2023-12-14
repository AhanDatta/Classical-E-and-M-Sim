#This file handles user input to fix initial conditions for the simulation
import numpy as np
from Particle_Class import Particle 

#Initialize list of all particles
particles = []
end_time = 0

#Notes the units of input
print("Note that this simulation uses SI units, so the results will be incorrect if data is input in a different system of units.")

#Main User Input Loop
while True:

    #Checks if user wants a new particle, and if not, exits the input loop
    create_new_particle = ""
    while not (create_new_particle == 'Y' or create_new_particle == 'N'):
        create_new_particle = input("Do you want to add a new particle? (Y/N): ")

    if create_new_particle == 'N':
        break
    
    #Gets the initial position of the new charge from the user
    position = np.zeros(3)
    while True:
        try:
            position[0] = float(input("Enter the x position of the particle (number): "))
            position[1] = float(input("Enter the y position of the particle (number): "))
            position[2] = float(input("Enter the z position of the particle (number): "))
            break
        except ValueError:
            print("Please enter only numbers for each position.")

    #Gets the initial velocity of the new charge from the user
    velocity = np.zeros(3)
    while True:
        try:
            velocity[0] = float(input("Enter the x velocity of the particle (number): "))
            velocity[1] = float(input("Enter the y velocity of the particle (number): "))
            velocity[2] = float(input("Enter the z velocity of the particle (number): "))
            break
        except ValueError:
            print("Please enter only numbers for each velocity.")

    #Gets the mass and charge from the user
    mass = 1
    charge = 1
    while True:
        try:
            mass = float(input("Enter the mass of the particle (number): "))
            charge = float(input("Enter the charge of the particle (number): "))
            break
        except ValueError:
            print("Please enter only numbers for mass and charge.")

    #Creates new particle and appends it to the list of particles
    particles.append(Particle(position, velocity, charge, mass))

#Gets ending time of the simulation
while not end_time > 0:
    try:
        end_time = float(input("How long do you want to run the simulation for? (number): "))
    except ValueError:
        print("Please enter only a positive number for the time.")