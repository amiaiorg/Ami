import unittest
from src.algorithms.harmonic_balancer import HarmonicBalancer
from src.algorithms.objective_function import custom_objective_function

class TestHarmonicBalancer(unittest.TestCase):
    def test_balance(self):
        balancer = HarmonicBalancer(num_qubits=4, max_iterations=1000, harmony_memory_size=20, objective_function=custom_objective_function)
        best_solution, best_score = balancer.run_experiment()
        self.assertIsNotNone(best_solution)
        self.assertIsNotNone(best_score)

if __name__ == "__main__":
    unittest.main()
