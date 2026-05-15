# Author            : Oluchi Aviwe Olebuike
# Date Created      : 09/05/2026
# Project title     : Quantum Algorithm Noise Analysis using QEC-Inspired Models
# File name:        : metrics.py
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

# contains analysis metrics for evaluating algorithm robustness
# specifically logical error rate: measures probability of failure relative to the expected logical state
# used to quantify noise-induced corruption, stability under decoherence, state degradation
def logical_error_rate(counts, target_state='11'):
    #  gets the logical error rate
    # LER  = 1 - P(correct state)
    total = sum(counts.values())
    correct = counts.get(target_state, 0)
    return 1 - (correct /total)
