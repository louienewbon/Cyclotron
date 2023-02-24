import numpy as np
import scipy.constants as cons
from Input import Input


class Cyclotron:
    def __init__(self, bfield, efield, f, dV, V1, V2, L):
        self.bfield = bfield
        self.efield = efield
        self.f = f
        self.dV = dV
        self.V1 = V1
        self.V2 = V2
        self.L = L

    bfield = np.array([0, 0, 1.5e-6], dtype=float)

    f = (Input.protonCharge * bfield)/(2 * cons.pi * Input.protonMass)

    V1 = 10
    V2 = 1
    dV = V1 - V2
    L = 0.05

    if Input.Proton.position[0] < L and Input.Proton.position[0] > -L:
        efield = dV / (2 * L) * np.sin(2 * cons.pi * f)
    else:
        efield = 0


    def __str__(self):
        return "STRENGTH OF FIELDS"

