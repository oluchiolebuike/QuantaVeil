# Author            : Oluchi Aviwe Olebuike
# Date Created      : 27/04/2026
# Last modified     : 15/05/2026
# Project title     : Quantum Algorithm Noise Analysis using QEC-Inspired Models
# File name:        : repetition.py
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

from qiskit import QuantumCircuit
class ThreeQubitRepetition:
    def __init__(self):
        self.n_qubits = 3

        # encode logical qubit
        # |0> to |000> etc.
        # uses CNOT fanout oprations

    def encode(self, qc: QuantumCircuit, logical_qubit=0):
        qc.cx(logical_qubit, 1)
        qc.cx(logical_qubit, 2)

        # injecting bit-flip error 
    def bitflip_error(self, qc: QuantumCircuit, qubit: int):
        qc.x(qubit)

        return qc
    
    # determines the most likely state by majority voting across measured qubits
    def majority_vote(self, state: str):
        ones = state.count('1')
        zeros = state.count('0')

        if ones > zeros:
            return '1'
        
        return '0'
    
    # full demo circuit
    def build_demo_circuit(self):
        qc = QuantumCircuit(3, 3)

        # logical |1>
        qc.x(0)

        # encoding qubit
        self.encode(qc)

        # simulated bit-flip error
        qc.x(1)

        qc.measure([0, 1, 2], [0, 1, 2])

        return qc



