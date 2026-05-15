# Author            : Oluchi Aviwe Olebuike
# Date Created      : 09/05/2026
# Last modified     : 15/05/2026
# Project title     : Quantum Algorithm Noise Analysis using QEC-Inspired Models
# File name         : noisy_runner.py
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

# executes quantum circuits under noisy simulation environments

from qiskit import transpile 
from qiskit_aer import AerSimulator

class NoisyRunner:

    def __init__(self, noise_model=None):
        self.simulator = AerSimulator(noise_model=noise_model)

    def run(self, circuit, shots=8192):# (might want to change shots during experimentation)

        compiled = transpile(circuit, self.simulator)

        result = self.simulator.run(compiled, shots=shots).result()

        return result.get_counts()
