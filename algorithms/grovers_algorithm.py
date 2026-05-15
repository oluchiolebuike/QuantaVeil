# Author            : Oluchi Aviwe Olebuike
# Date Created      : 09/05/2026
# Project title     : Quantum Algorithm Noise Analysis using QEC-Inspired Models
# File name         : grovers_algorithm.py
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
# pip install qiskit qiskit-aer matplotlib numpy pandas seaborn

from qiskit import QuantumCircuit

# in grover's algorithm the oracle flips the phase of the target state to distinguish
# it from all other computational basis states
def grover_oracle(circuit):
    # oracle marking : |11>
    # flip |11> using CZ
    circuit.cz(0, 1)
    # circuit.cx(0, 1) 
    # circuit.cx(1, 0)

# apply the grover diffusion operator 
# the diffuser performs inversion about the mean, amplifying the probability
# amplitude of the marked state
def grover_diffuser(circuit):
    # diffuser (inversion about the mean)
    # amplify |11> upward

    # move to computational basis
    circuit.h([0, 1])

    #reflect about |00>
    circuit.x([0, 1])

    # phase inversion
    circuit.cz(0, 1)  # marks |11> : |00> after x

    # undoing the reflection
    circuit.x([0, 1])

    # return to superposition basis
    circuit.h([0, 1])

# creates full 2-qubit grover search circuit from the initialised superposition after applying
# the oracle and diffuser
def build_grover() -> QuantumCircuit:
    # build circuit
    qc = QuantumCircuit(2, 2)

    # superposition
    qc.h([0, 1])

    # oracle
    grover_oracle(qc)

    # diffuser
    grover_diffuser(qc)

    # measure output states 
    qc.measure([0, 1], [0, 1])

    return qc