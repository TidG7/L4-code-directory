import qutip as qt
import numpy as np
from IPython.display import HTML
import matplotlib.pyplot as plt
H = qt.tensor(qt.sigmaz(),qt.qeye(2))

psi0 = (qt.ket('10')+qt.ket('01')).unit()

tlist = np.linspace(0, 3*np.pi, 100)
results = qt.mesolve(H, psi0, tlist, [], [])
# fig, ani = qt.anim_schmidt(results)
# plt.show()

compl_circ = np.array([[(x + 1j*y) if x**2 +y**2 <= 1 else 0j
                        for x in np.arange(-1, 1, 0.005)]
                       for y in np.arange(-1, 1, 0.005)])
fig = plt.figure(figsize=(7, 3))
ax0 = plt.subplot(1, 2, 1)
ax1 = plt.subplot(1, 2, 2)
ax1.set_xlabel("x", fontsize=14)
ax1.set_ylabel("y", fontsize=14)
ax1.imshow(qt.complex_array_to_rgb(compl_circ, rmax=1, theme='light'),
           extent=(-1, 1, -1, 1))
plt.tight_layout()
fig, ani = qt.anim_schmidt(results, fig=fig, ax=ax0)
plt.show()