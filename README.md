# QuantaVeil
QuantaVeil is a starter project that simulates a quantum computer, demonstrating core concepts such as quantum circuits, basic quantum algorithms and result visualization using Qiskit. The goal is to build intuition for how quantum computers operate through practical simulation.

The name came from combining two ideas:

“Quanta” → quantum computing (qubits, superposition, algorithms like Grover’s)
“Veil” → something hidden or abstract being revealed (like uncovering how quantum systems behave through simulation)

So the meaning behind it is basically:

QuantaVeil = revealing the hidden world of quantum computation through simulation


## Installation

Install the required dependencies before running the project:

```bash
pip install qiskit qiskit-aer matplotlib pylatexenc
```

## Results Analysis

The simulation was executed 7 times to observe the behaviour of Grover’s Algorithm on a 2-qubit system targeting the state |11⟩.


## What we observed

Across repeated runs:

- The probabilities of all states (|00⟩, |01⟩, |10⟩, |11⟩) remain relatively close (around 0.23–0.28)
- The most likely state changes between runs:
  - Sometimes |11⟩ appears as the highest probability
  - Other times |00⟩ or |01⟩ becomes dominant
- No single state is consistently dominant across all executions


## Interpretation

In an ideal Grover’s Algorithm implementation, the target state (|11⟩) should consistently have the highest probability.

However, in this simulation:

- The system behaves partially like a uniform quantum superposition
- The amplification of the target state is weak and inconsistent
- The circuit is effectively running a minimal Grover iteration, where quantum interference effects remain probabilistic rather than deterministic

## What this simulation does (simple explanation)

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

## Future Improvements

Create a full stack system for QuantaVeil using React, FastAPI or Flask & between D3.js or React-Vis 

## How the new updated system will work
- Quantum Circuit Builder: Allow users to drag and drop quantum gates (e.g., Hadamard, Pauli-X) onto qubits. This could be a grid or a timeline-style UI where users can see the circuit evolving as they add gates. 
- Quantum State Visualizer: Once the circuit is created, provide real-time visualizations (like Bloch Sphere for individual qubits, histograms for measurement outcomes). 
- Run Simulation: After constructing the quantum circuit, users can click a "Run Simulation" button. This will send the circuit to the backend, where it will be simulated using your existing quantum logic, and the results (measurement outcomes) will be returned and visualized on the frontend.
- Results Display: Display the simulation results in a visually appealing way, such as a histogram showing the measurement probabilities or a bloch sphere visualization showing quantum state rotations. 


## Key takeaway

Even in this simplified simulation, a core principle of quantum computing is demonstrated:

Quantum algorithms do not produce fixed answers. Instead, they amplify probabilities, meaning outcomes can vary across runs unless the amplification is sufficiently strong.
