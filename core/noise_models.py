# Author            : Oluchi Aviwe Olebuike
# Date Created      : 27/04/2026
# Last modified     : 15/05/2026
# Project title     : Quantum Algorithm Noise Analysis using QEC-Inspired Models
# File name         : noise_models.py
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


from qiskit_aer.noise import NoiseModel
from qiskit_aer.noise.errors import (depolarizing_error, 
                                     thermal_relaxation_error,
                                     pauli_error)

# deplorization 
# depolarization errors consist of random X,Y,Z rotations caused by intrinisic coupling of the qubit environment. this happens when you apply gate operations
# different gates appled to the density matrix ased on a probaility
# therefore, if low chance of error
# the probability will be low

# relaxation & dephasing
# because qubits experience decoherence and dephasing as time passes depending on the temp of the environment, relaxation and dephasing error models can be used
# apply these errors discretely after each circuit gate operation when applying time-dependent operations
# T1 is the evolution towards the equilibrium state at the temp of the environment
# dephasing : transition of quantum state to a classical one - environmental coupling

# creates a realistic superconducting qubit noise model
def depolarization_model(p1=0.01, t1: float = 50e3, t2: float = 70e3, gate_time_1q: float =50, gate_time_2q: float = 300):
    
    noiseModel = NoiseModel()

    # depolarization errors
    error_1q = depolarizing_error(p1, 1)
    error_2q = depolarizing_error(p1 * 2, 2)

    # thermal relaxation
    therma_1q = thermal_relaxation_error(t1, t2, gate_time_1q)
    therma_2q = thermal_relaxation_error(t1, t2, gate_time_2q).tensor(thermal_relaxation_error(t1, t2, gate_time_2q))

    # combining noise
    combined_1q = error_1q.compose(therma_1q)
    combined_2q = error_2q.compose(therma_2q)

    # applying to gates
    noiseModel.add_all_qubit_quantum_error(combined_1q, ['h', 'x'])

    # applying to gates
    noiseModel.add_all_qubit_quantum_error(combined_2q, ['cx', 'cz'])

    return noiseModel











