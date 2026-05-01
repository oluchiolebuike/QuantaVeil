# QuantaVeil
QuantaVeil is a starter project that I've started to reveal the hidden world of quantum computation through a simulation of a quantum computer, demonstrating core concepts such as quantum circuits, basic quantum algorithms and result visualization using Qiskit. The goal is to build intuition for how quantum computers operate through practical simulation.

The name came from combining two ideas:

- “Quanta” : quantum computing (qubits, superposition, algorithms like Grover’s)
- “Veil” : something hidden or abstract being revealed (like uncovering how quantum systems behave through simulation)


## Installation

Install the required dependencies before running the project:

```bash
pip install qiskit qiskit-aer matplotlib pylatexenc
```

## Results Analysis

The simulation was executed 7 times to observe the behaviour of Grover’s Algorithm on a 2-qubit system targeting the state |11⟩.


## What we observed

Day 1:
- The probabilities of all states (|00⟩, |01⟩, |10⟩, |11⟩) remain relatively close (around 0.23–0.28)
- The most likely state changes between runs:
  - Sometimes |11⟩ appears as the highest probability
  - Other times |00⟩ or |01⟩ becomes dominant
- No single state is consistently dominant across all executions

Day 2:
- Final Result (8192 shots):
- |11⟩: 1.000 — perfect amplification
- All other states: 0.000
- We increased the number of shots from 1024 to 8192 which destroyed every non-target state (|00⟩, |01⟩, |10⟩) which is a destructive quantum interference tec

- Grover's Algorithm confirmed deterministic target identification for N=4 in exactly 1 iteration.

## Interpretation

In an ideal Grover’s Algorithm implementation, the target state (|11⟩) should consistently have the highest probability (1.0).

Day 1:
However, in this simulation:

- The system behaves partially like a uniform quantum superposition
- The amplification of the target state is weak and inconsistent
- The circuit is effectively running a minimal Grover iteration, where quantum interference effects remain probabilistic rather than deterministic

Day 2:
- System now is deterministic rather than being probabibalistic 
- The amplitude of every non-target state was completely cancelled through destructive quantum interference, while |11⟩ was amplified to certainty through constructive interference

## What this simulation does 

This project simulates a small quantum computer using Qiskit and demonstrates the core ideas behind Grover’s Algorithm:

- Creates a superposition of all possible 2-qubit states : the system explores all solutions at once

- Applies an oracle : attempts to mark the target state (|11⟩)

- Applies a diffuser (amplification step) : increases the probability of the marked state

- Measures the system multiple times (1024 shots) : collapses the quantum state into classical results



## What is visualized

The program outputs:

- Probability distribution of all quantum states  
- Most likely measured state per run  
- Quantum circuit diagram (optional visualization)  

These visualizations show how quantum probability distributions evolve after applying Grover’s Algorithm.


