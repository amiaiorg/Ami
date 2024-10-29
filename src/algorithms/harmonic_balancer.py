
# algorithm/harmonic_balancer.py

import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from .quantum_system import QuantumSystem
from ..utils.helpers import phi_pi_transition, generate_harmony_vector, state_to_dna, count_valid_codons, calculate_gc_content, calculate_base_balance

class HarmonicBalancer:
    def __init__(self, num_qubits, max_iterations, harmony_memory_size, objective_function=None, convergence_threshold=1e-6):
        self.num_qubits = num_qubits
        self.max_iterations = max_iterations
        self.harmony_memory_size = harmony_memory_size
        self.harmony_memory = [generate_harmony_vector(num_qubits) for _ in range(harmony_memory_size)]
        self.best_solution = None
        self.best_score = -np.inf
        self.history = {'scores': [], 'states': []}
        self.quantum_system = QuantumSystem(num_qubits)
        self.objective_function = objective_function if objective_function else self.default_objective_function
        self.convergence_threshold = convergence_threshold

    def default_objective_function(self, vector, param=1):
        return np.sum(vector) * param

    def run_experiment(self):
        for iteration in range(self.max_iterations):
            new_harmony_vector = self.generate_new_harmony(transition_constant=0.1)
            evolved_state = new_harmony_vector
            score = self.objective_function(evolved_state)
            self.update_harmony_memory(new_harmony_vector, evolved_state, score)
            self.history['scores'].append(score)
            self.history['states'].append(evolved_state)
            self.quantum_system.update_parameters(evolved_state, score, transition_constant=0.1)
            
            if iteration > 0 and abs(self.history['scores'][-1] - self.history['scores'][-2]) < self.convergence_threshold:
                print(f"Convergence achieved at iteration {iteration}")
                break

        return self.best_solution, self.best_score

    def generate_new_harmony(self, transition_constant):
        selected_index = np.random.randint(self.harmony_memory_size)
        selected_vector = self.harmony_memory[selected_index]
        perturbation = np.random.normal(0, transition_constant / 10, size=len(selected_vector))
        new_vector = selected_vector + perturbation
        new_vector = np.clip(new_vector, 0, 1)
        return new_vector

    def update_harmony_memory(self, new_harmony_vector, evolved_state, score):
        if score > self.best_score:
            self.best_solution = evolved_state
            self.best_score = score
        worst_index = np.argmin([self.objective_function(harmony) for harmony in self.harmony_memory])
        self.harmony_memory[worst_index] = new_harmony_vector