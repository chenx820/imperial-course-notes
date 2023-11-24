"""
Author: Chen Huang
Date: 22 Nov 2023
"""

import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# Create a random mixed quantum state
psi = (tensor(rand_ket(2), rand_ket(2)) + tensor(rand_ket(2), rand_ket(2))) / np.sqrt(2)
rho = ket2dm(psi)  # Convert to a density matrix

# Visualisation
hinton(rho)
plt.savefig('density-matrix-visualisation.png')
plt.show()
