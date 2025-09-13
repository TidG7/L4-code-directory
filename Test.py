import scipy
import numpy
import matplotlib.pyplot
import qutip
#!/usr/bin/env python
# coding: utf-8

# # Decomposition of the Toffoli gate in terms of CNOT and single-qubit rotations

from qutip import about
from qutip_qip.operations import gate_sequence_product
from qutip_qip.circuit import QubitCircuit

q = QubitCircuit(3, reverse_states=False)
q.add_gate("TOFFOLI", controls=[0, 2], targets=[1])

q.draw()

U = gate_sequence_product(q.propagators())

U.tidyup()


q2 = q.resolve_gates()
q2.draw()


U2 = gate_sequence_product(q2.propagators())

U2.tidyup()

U == U2
