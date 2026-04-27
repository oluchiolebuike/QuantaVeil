# SETUP 
# run : pip install qiskit qiskit-aer matplotlib pylatexenc
# then run program file

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# grover's algorithm

def grover_oracle(circuit):
    """oracle marking |11>"""
    circuit.cz(0, 1)
    # circuit.cx(0, 1) 
    # circuit.cx(1, 0)

def grover_diffuser(circuit):
    """diffuser (inversion about the mean)"""
    circuit.h([0, 1])
    circuit.x([0, 1])
    circuit.cz(0, 1)
    circuit.x([0, 1])
    circuit.h([0, 1])

# build circuit
qc = QuantumCircuit(2, 2)

# superposition
qc.h([0, 1])

# oracle
grover_oracle(qc)

# diffuser
grover_diffuser(qc)

# measurement
qc.measure([0, 1], [0, 1])

# simulation
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit, shots=1024).result()

# results
counts = result.get_counts()

# sort results (00, 01, 10, 11)
counts = dict(sorted(counts.items()))



plot_histogram(counts, title="Grover Search Results (Target = |11⟩)", color='midnightblue')
plt.tight_layout()
plt.show()

# circuit diagram
print("\nQuantum Circuit:")
qc.draw('mpl')
plt.show()


# probabilities
total = sum(counts.values())
print("\nProbabilities:")
for state, count in counts.items():
    print(f"{state}: {count/total:.3f}")

# highlight most likely state
target = max(counts, key=counts.get)
print(f"\nMost likely state: |{target}>")
