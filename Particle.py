import numpy as np


class Particle:

    def __init__(self, position, velocity,
                 acceleration, name='', charge=(), mass=()):
        self.name = name
        self.mass = mass
        self.charge = charge
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    position = np.array([0, 0, 0], dtype=float)
    velocity = np.array([0, 0, 0], dtype=float)
    acceleration = np.array([0, 0, 0], dtype=float)

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration)

    def euler_cromer(self, deltaT):
        self.velocity = self.velocity + (self.acceleration * deltaT)
        self.position = self.position + (self.velocity * deltaT)

    def update_acceleration(self, bfield, efield):
        self.acceleration = np.array([0, 0, 0], dtype=float)
        self.acceleration = self.acceleration + (self.charge * np.cross(self.velocity, bfield))/self.mass + (self.charge * efield)/self.mass



