from src.algorithms.harmonic_balancer import HarmonicBalancer
from src.algorithms.objective_function import custom_objective_function

def run_experiment():
    balancer = HarmonicBalancer(num_qubits=4, max_iterations=1000, harmony_memory_size=20, objective_function=custom_objective_function)
    best_solution, best_score = balancer.run_experiment()
    return best_solution, best_score