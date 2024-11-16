import unittest
import numpy as np
from src.algorithms.harmonic_balancer import HarmonicBalancer

def custom_objective_function(vector):
    return np.sum(vector)

class TestHarmonicBalancer(unittest.TestCase):

    def test_balance(self):
        balancer = HarmonicBalancer(num_qubits=4, max_iterations=1000, harmony_memory_size=20, objective_function=custom_objective_function)
        best_solution, best_score = balancer.run_experiment()
        self.assertIsNotNone(best_solution)
        self.assertIsInstance(best_score, float)

if __name__ == "__main__":
    unittest.main()
