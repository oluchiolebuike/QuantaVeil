# run : pip install qiskit qiskit-aer matplotlib pylatexenc

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit_aer import AerSimulator # deutsch algo
from qiskit import transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# grover's algorithm

def grover_oracle(circuit):
    # oracle marking |11>
    # flip |11> using CZ
    circuit.cz(0, 1)
    # circuit.cx(0, 1) 
    # circuit.cx(1, 0)

def grover_diffuser(circuit):
    # diffuser (inversion about the mean)
    # amplify |11> upward
    # note: maybe it didn't invert about the correct mean
    circuit.h([0, 1])
    circuit.x([0, 1])
    circuit.cz(0, 1)  # marks |11> : |00> after x
    circuit.x([0, 1])
    circuit.h([0, 1])
    
# deutsch's algorithm

def deutsch(case:int):
    # function generates a quantum circuit for 1 OI from one bit to one bit
    if case not in [1, 2, 3, 4]:
        raise ValueError("'case' must be 1, 2, 3 or 4.")

    f = QuantumCircuit(2)
    if case in [2, 3]:
        f.cx(0, 1)
    
    if case in [3, 4]:
        f.x(1)
    return f

# compile circuit for deutsch
def compile_circuit(function: QuantumCircuit):

    n = function.num_qubits - 1
    qc = QuantumCircuit(n + 1, n)

    qc.x(n)
    qc.h(range(n + 1))

    qc.barrier()
    qc.compose(function, inplace=True)
    qc.barrier()

    qc.h(range(n))
    qc.measure(range(n), range(n))

    return qc
# run deutsch algorithm   
def deutsch_algorithm(function: QuantumCircuit):
    
    qc = compile_circuit(function)

    simulator = AerSimulator()
    result = simulator.run(qc, shots=1024).result()
    counts = result.get_counts()

    # majority decision
    if counts.get('0', 0) > counts.get('1', 0):
        return "constant"
    return "balanced"

# test deutsch
f = deutsch(1)
print("Deutsch result:", deutsch_algorithm(f))

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
# result = simulator.run(compiled_circuit, shots=1024).result()
result = simulator.run(compiled_circuit, shots=8192).result() # increased shots from 1024 to 8192 to account for shot noise 

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
qc.draw('text') # verifying gate order
plt.show()


# probabilities
total = sum(counts.values())
print("\nProbabilities:")
for state, count in counts.items():
    print(f"{state}: {count/total:.3f}")
# the most likely state should be target state |11> 
# P = 1.0

# highlight most likely state
max_count = max(counts.values())

most_likely_states = [state for state, count in counts.items() if count == max_count]

print(f"\nMax probability count: {max_count}")
print("Most likely state(s):")

for state in most_likely_states:
    print(f"|{state}>")
