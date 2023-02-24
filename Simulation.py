import numpy as np
from Cyclotron import Cyclotron as cy
from Particle import Particle as par
from Input import Input
from matplotlib import pyplot as plt


Pos = []
xpos = []
ypos = []
L = []
minusL = []

Acc = []

time = 0
totTime = []

bfield = cy.bfield
efield = cy.efield


for i in range(1000):

    par.update_acceleration(Input.Proton, bfield, efield)
    par.euler_cromer(Input.Proton, 1e-3)

    time = time + 1e-3
    totTime.append(time)

    Pos.append(Input.Proton.position)

    Acc.append(np.linalg.norm(Input.Proton.acceleration))


fig = plt.figure()
ax = plt.axes()
ax.set_title("Cyclotron")
ax.set_xlabel("x position (m)")
ax.set_ylabel("y position (m)")


fig.set_size_inches(8, 8)


for i in range(len(Pos)):
    #print(Pos[i][0], Pos[i][1])
    xpos.append(Pos[i][0])
    ypos.append(Pos[i][1])


plt.plot(xpos, ypos)
plt.vlines(x=0.001, ymin=-5, ymax=5, colors='red')
plt.vlines(x=-0.001, ymin=-5, ymax=5, colors='red')
ymax = max(ypos) + 0.05*max(ypos)
ymin = min(ypos) + 0.05*min(ypos)

#plt.ylim(ymax, ymin)
#plt.plot(Acc, totTime)

plt.show()

print()