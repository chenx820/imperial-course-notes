"""
This script generates Wigner functions for four different quantum states: a coherent state, a thermal state, a Fock
state, and a squeezed state. These states are represented in a phase space using QuTiP, a Python library for quantum
mechanics and quantum optics. The Wigner functions are then plotted as contour plots.

Author: Chen Huang
Date: 22 Nov 2023
"""

import numpy as np
import matplotlib.pyplot as plt
from qutip import *

N = 20  # The number of states
vac = basis(N, 0)  # Vacuum state
xvec = np.linspace(-4, 4, 100)

# Generate density matrices for different states
rho_coherent = coherent_dm(N, np.sqrt(2))
rho_thermal = thermal_dm(N, 2)
rho_fock = fock_dm(N, 2)
rho_squeezed = ket2dm(squeeze(N, complex(0.5, 0.25)) * vac)

# Calculate the Wigner function for each state
W_coherent = wigner(rho_coherent, xvec, xvec)
W_thermal = wigner(rho_thermal, xvec, xvec)
W_fock = wigner(rho_fock, xvec, xvec)
W_squeezed = wigner(rho_squeezed, xvec, xvec)

# Store the states and their corresponding Wigner functions in a dictionary
W_states = {
    "Coherent State": W_coherent,
    "Thermal State": W_thermal,
    "Fock State": W_fock,
    "Squeezed State": W_squeezed
}

# Create a figure for the Wigner functions
fig, axes = plt.subplots(1, 4, figsize=(13, 3))

# Loop over the states and their corresponding Wigner functions
for ax, (state, W) in zip(axes, W_states.items()):
    cont = ax.contourf(xvec, xvec, W, 100)
    ax.set_title(state)
    ax.set_xticks([-4, 0, 4])
    ax.set_yticks([-4, 0, 4])

plt.savefig('wigner-function.png')
plt.show()
