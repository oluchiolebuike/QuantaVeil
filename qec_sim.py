# Author            : Oluchi Aviwe Olebuike
# Date Created      : 27/04/2026
# Last modified     : 15/05/2026
# Project title     : Quantum Algorithm Noise Analysis using QEC-Inspired Models
# File name         : qec_sim.py
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

from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

from core.noisy_runner import NoisyRunner
from core.noise_models import depolarization_model

from algorithms.deutsch_algorithm import deutsch, compile_circuit
from algorithms.grovers_algorithm import build_grover

from analysis.metrics import logical_error_rate

# noise environment setup
noise = depolarization_model(0.05)
sim = NoisyRunner(noise_model=noise)

# deutsch algorithm analysis
print("Deutsch's Algorithm (Noisy Simulation)")

for case in [1, 2, 3, 4]:
    oracle = deutsch(case)
    qc = compile_circuit(oracle)
    counts = sim.run(qc, shots=8192)# used to mitigate the effects of hardware noise and should not affect theoretical output of algorithm (might adjust shots again for experiment) 
    print(f"Case {case}: {counts}")

# grovers algorithm analysis
print("\nGrover's Search Algorithm (Noisy Simulation)")
qc = build_grover()
counts = sim.run(qc, shots=8192) # 8192 shots used to mitigate the effects of hardware noise (might change during experimentation)
print(counts)

# LER
ler = logical_error_rate(counts, '11') # target state set to |11>
print(f"\nLogical Error Rate: {ler:.6f}")

# probability distribution
print("\nProbabilities:")
total = sum(counts.values())

for state, c in counts.items():
    prob = c / total
    print(f"{state}: {prob:.4f}")
