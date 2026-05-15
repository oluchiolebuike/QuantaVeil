# Author            : Oluchi Aviwe Olebuike
# Date Created      : 27/04/2026
# Last modified     : 15/05/2026
# Project title     : Quantum Algorithm Noise Analysis using QEC-Inspired Models
# File name:        : repetition_demo.py
# Modernised        : Qiskit 2.x / qiskit-aer 0.17+


# Description:
# This experiment evaluates the robustness of quantum algorithms under
# realistic superconducting qubit noise environments

# The simulation framework studies the impact of:
# Relaxation Errors (T1 Decoherence)
# Dephasing Errors (T2 Decoherence)
# Depolarization Noise


# on the following quantum algorithms:
# Deutsch's Algorithm
# Grover's Search Algorithm

# The objective is to investigate:
# Logical state degradation
# Noise sensitivity
# Probability distribution drift
# Algorithm stability under increasing decoherence

# Installations:
# pip install qiskit qiskit-aer matplotlib numpy pandas seaborn pylatexenc

from qiskit_aer import AerSimulator
from qiskit import transpile

from qec.repetition import ThreeQubitRepetition

code = ThreeQubitRepetition()

# building circuit - just an example from experimentation
qc = code.build_demo_circuit()

sim = AerSimulator()

# executing our simulator using repetition code 
compiled = transpile(qc, sim)
result = sim.run(compiled, shots=8192).result()
counts = result.get_counts()

print("Counts:", counts)

# decode logical states
for state in counts:
    decoded = code.majority_vote(state)
    print(f"{state}: logical|{decoded}")
