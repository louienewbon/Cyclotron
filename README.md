# Cyclotron

A 3-D simulation of a non-relativistic cyclotron particle accelerator. Eventually, the simulation will take bunches of particles and accelerate them using a magnetic field described with user input.

Cyclotron.py contains the conditions of the magnetic and electric fields - the "settings" of the cyclotron.

Input.py contains the initial conditions of the particles (using Particle class from Particle.py) that will be accelerated. Right now, it only contains the properties of a proton. Eventually, it will allow for bunches.

Particle.py contains the Particle class which initialises the characteristics of the particles for use in Input.py.

Simulation.py runs the simulation, and contains values for the time step and the code responsible for plotting the data generated.
