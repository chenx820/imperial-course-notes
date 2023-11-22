import numpy as np
import matplotlib.pyplot as plt
from qutip import *

N = 20  # The number of states
vac = basis(N, 0)  # Vacuum state

# Define a range of values for the x-axis for our Wigner functions
xvec = np.linspace(-4, 4, 100)

# Generate a density matrix for a coherent state with a mean photon number of sqrt(2)
rho_coherent = coherent_dm(N, np.sqrt(2))

# Generate a density matrix for a thermal state with an average photon number of 2
rho_thermal = thermal_dm(N, 2)

# Generate a density matrix for a Fock (number) state with exactly 2 photons
rho_fock = fock_dm(N, 2)

# Generate a density matrix for a squeezed state with a squeezing parameter
rho_squeezed = ket2dm(squeeze(N, complex(0.5, 0.25)) * vac)

# Calculate the Wigner function for each of these states
W_coherent = wigner(rho_coherent, xvec, xvec)
W_thermal = wigner(rho_thermal, xvec, xvec)
W_fock = wigner(rho_fock, xvec, xvec)
W_squeezed = wigner(rho_squeezed, xvec, xvec)

# Create a figure with 4 subplots, one for each Wigner function
fig, axes = plt.subplots(1, 4, figsize=(15, 3))

# Plot the Wigner function for the coherent state
cont0 = axes[0].contourf(xvec, xvec, W_coherent, 100)
lbl0 = axes[0].set_title("Coherent State")

# Plot the Wigner function for the thermal state
cont1 = axes[1].contourf(xvec, xvec, W_thermal, 100)
lbl1 = axes[1].set_title("Thermal State")

# Plot the Wigner function for the Fock state
cont2 = axes[2].contourf(xvec, xvec, W_fock, 100)
lbl2 = axes[2].set_title("Fock State")

# Plot the Wigner function for the squeezed state
cont3 = axes[3].contourf(xvec, xvec, W_squeezed, 100)
lbl3 = axes[3].set_title("Squeezed State")

# Add a colorbar to the right of the plots
fig.colorbar(cont3, ax=axes.ravel().tolist())

plt.savefig('wigner-function-fig.png')
plt.show()
