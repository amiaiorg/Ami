import unittest
import numpy as np
from src.algorithms.quantum_system import QuantumSystem

class TestQuantumSystem(unittest.TestCase):

    def setUp(self):
        self.num_states = 4
        self.quantum_system = QuantumSystem(self.num_states)

    def test_initial_parameters(self):
        self.assertTrue(np.array_equal(self.quantum_system.get_parameters(), np.zeros(self.num_states)))

    def test_update_parameters(self):
        state = np.array([1, 0, 0, 0])
        score = 1.0
        transition_constant = 0.1
        self.quantum_system.update_parameters(state, score, transition_constant)
        expected_parameters = transition_constant * score * state
        self.assertTrue(np.allclose(self.quantum_system.get_parameters(), expected_parameters))

    def test_reset_parameters(self):
        state = np.array([1, 0, 0, 0])
        score = 1.0
        transition_constant = 0.1
        self.quantum_system.update_parameters(state, score, transition_constant)
        self.quantum_system.reset_parameters()
        self.assertTrue(np.array_equal(self.quantum_system.get_parameters(), np.zeros(self.num_states)))

    def test_evolve_state(self):
        state = np.array([1, 0, 0, 0])
        evolved_state = self.quantum_system.evolve_state(state, steps=1)
        self.assertEqual(evolved_state.shape, (self.num_states,))
        self.assertAlmostEqual(np.linalg.norm(evolved_state), 1.0)

    def test_invalid_state_vector(self):
        with self.assertRaises(ValueError):
            invalid_state = np.array([1, 0, 0])  # Invalid shape
            self.quantum_system.evolve_state(invalid_state)

if __name__ == "__main__":
    unittest.main()