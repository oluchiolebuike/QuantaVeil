# QuantaVeil
QuantaVeil is a starter project that I've started to reveal the hidden world of quantum computation through a simulation of a quantum computer, demonstrating core concepts such as quantum circuits, basic quantum algorithms and result visualization using Qiskit. The goal is to build intuition for how quantum computers operate through practical simulation.

The name came from combining two ideas:

- “Quanta” : quantum computing (qubits, superposition, algorithms like Grover’s)
- “Veil” : something hidden or abstract being revealed (like uncovering how quantum systems behave through simulation)

QuantaVeil is now a quantum computing simulation framework developed using Qiskit to investigate how quantum algorithms behave under realistic superconducting qubit noise environments.

The project evaluates the robustness and stability of fundamental quantum algorithms such as Deutsch's Algorithm and Grover's Search Algorithm under multiple quantum noise models including depolarization, relaxation (T1 decoherence) and dephasing (T2 decoherence).

The framework incorporates QEC-inspired simulation techniques, noisy circuit execution, logical error rate analysis, probability distribution tracking and repetition-code-based error mitigation to study:

Logical state degradation
Noise sensitivity
Decoherence effects
Probability drift
Algorithm reliability under increasing quantum noise

The project was modernised for Qiskit 2.x and Qiskit Aer 0.17+, providing a modular experimental environment for quantum algorithm benchmarking, quantum error correction research and noisy intermediate-scale quantum (NISQ) system analysis.


