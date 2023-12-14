#This file defines the main particle of the simulation
import numpy as np

#Radius defined so that behaviour of two particles with close locations is non-singular
PARTICLE_RADIUS = 0.1

#Class definition for partcle in simulation
class Particle:

    #Position given in a numpy 3-array, charge and mass are floats
    def __init__(self, position, velocity, charge, mass) -> None:
        self.position = position
        self.velocity = velocity
        self.charge = charge
        self.mass = mass

    #Gets the electric field vector (E = q/r^2 * r^\hat) at location from particle not adjusted for constants, except when the location is on the particle itself
    def e_field (self, r):
        r_magnitutde = np.linalg.norm(r)
        if r_magnitutde > PARTICLE_RADIUS:
            return (r) * self.charge/(r_magnitutde**3)
        else:
            return 0
    
    #Gets teh resultant magnetic field vector (B = (qv x r^\hat)/(r * r)) at location not adjusted for constants, except when the location is on the particle itself
    def B_field (self, r):
        r_magnitutde = np.linalg.norm(r)
        if r_magnitutde > PARTICLE_RADIUS:
            return self.charge * np.cross(self.velocity, r)/(r_magnitutde**3)
        else:
            return 0

