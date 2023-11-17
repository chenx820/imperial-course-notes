import matplotlib.pyplot as plt
import numpy as np
from qutip import *

N = 20
rho_coherent = coherent_dm(N, np.sqrt(2))
rho_thermal = thermal_dm(N, 2)
rho_fock = fock_dm(N, 2)
fig, axes = plt.subplots(1, 3, figsize=(12, 3))
plot_fock_distribution(rho_coherent, fig=fig, ax=axes[0], title='Coherent State')
plot_fock_distribution(rho_thermal, fig=fig, ax=axes[1], title='Thermal State')
plot_fock_distribution(rho_fock, fig=fig, ax=axes[2], title='Fock State')
fig.tight_layout()
plt.show()
