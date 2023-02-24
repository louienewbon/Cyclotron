import numpy as np
from Particle import Particle

class Input:

    protonMass = 1.6726e-27
    protonCharge = 1.6e-19
    Proton = Particle(
        position=np.array([0, 0, 0], dtype=float), velocity=np.array([0.5, 0, 0], dtype=float),
        acceleration=np.array([0, 0, 0], dtype=float),
        name="Proton",
        mass=protonMass,
        charge=protonCharge)
