"""
This script generates Wigner functions for four different quantum states: a coherent state, a thermal state, a Fock
state, and a squeezed state. These states are represented in a phase space using QuTiP, a Python library for quantum
mechanics and quantum optics. The Wigner functions are then plotted as contour plots.

Author: Chen Huang
Date: 28 Jan 2024
"""

import numpy as np
import matplotlib.pyplot as plt
from qutip import *

N = 20  # Dimension of the Hilbert space
vac = basis(N, 0)  # Vacuum state
xvec = np.linspace(-4, 4, 100)

# Generate density matrices for different states
# Fock state
rho_fock = fock_dm(N, 2)
# Thermal state
rho_thermal = thermal_dm(N, 2)
# Coherent state
alpha = complex(1.0, 1.0)  # Displacement parameter (complex value generally)
coherent_state = coherent(N, alpha)
rho_coherent = coherent_dm(N, alpha)  # Coherent state
# Coherent squeezed state
chi = complex(0.25, 0.5)  # Squeezed parameter
rho_coherent_squeezed = ket2dm(squeeze(N, chi) * coherent_state)

# Calculate the Wigner function for each state
W_fock = wigner(rho_fock, xvec, xvec)
W_thermal = wigner(rho_thermal, xvec, xvec)
W_coherent = wigner(rho_coherent, xvec, xvec)
W_coherent_squeezed = wigner(rho_coherent_squeezed, xvec, xvec)

# Store the states and their corresponding Wigner functions in a dictionary
W_states = {
    "Fock State": W_fock,
    "Thermal State": W_thermal,
    "Coherent State": W_coherent,
    "Coherent Squeezed State": W_coherent_squeezed
}

# Create a figure
fig, axes = plt.subplots(1, 4, figsize=(17, 4), gridspec_kw={'width_ratios': [1, 1, 1, 1]})

# Reduce whitespace on the left and right of the figure
plt.subplots_adjust(left=0.05, right=0.9)

for ax, (state, W) in zip(axes, W_states.items()):
    cont = ax.contourf(xvec, xvec, W, 100)
    ax.set_title(state)
    ax.set_xticks([-4, 0, 4])
    ax.set_yticks([-4, 0, 4])
    ax.set_aspect('equal')  # Set aspect ratio to 1:1

# Add a colorbar on the right side of the figure
cbar_ax = fig.add_axes([0.93, 0.1, 0.01, 0.78])  # Parameters are [left, bottom, width, height]
fig.colorbar(cont, cax=cbar_ax)

plt.savefig('wigner-distribution.png')
plt.show()
