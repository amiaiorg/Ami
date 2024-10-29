import unittest
import numpy as np
from src.algorithms.quantum_system import QuantumSystem
from src.algorithms.harmonic_balancer import HarmonicBalancer

class TestQuantumSystem(unittest.TestCase):

    def setUp(self):
        self.num_qubits = 4
        self.quantum_system = QuantumSystem(self.num_qubits)

    def test_initial_parameters(self):
        self.assertTrue(np.array_equal(self.quantum_system.get_parameters(), np.zeros(self.num_qubits)))

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
        self.assertTrue(np.array_equal(self.quantum_system.get_parameters(), np.zeros(self.num_qubits)))

    def test_evolve_state(self):
        state = np.array([1, 0, 0, 0])
        evolved_state = self.quantum_system.evolve_state(state, steps=1)
        self.assertEqual(evolved_state.shape, (self.num_qubits,))
        self.assertAlmostEqual(np.linalg.norm(evolved_state), 1.0)

    def test_invalid_state_vector(self):
        with self.assertRaises(ValueError):
            invalid_state = np.array([1, 0, 0])  # Invalid shape
            self.quantum_system.evolve_state(invalid_state)

    def test_encode_dna_sequence(self):
        sequence = "ATCG"
        encoded_state = self.quantum_system.encode_dna_sequence(sequence)
        self.assertEqual(encoded_state.shape, (self.num_qubits,))
        self.assertAlmostEqual(np.linalg.norm(encoded_state), 1.0)

class TestHarmonicBalancer(unittest.TestCase):
    def setUp(self):
        self.harmonic_balancer = HarmonicBalancer(num_qubits=4, max_iterations=1000, harmony_memory_size=20)

    def test_apply_golden_harmony(self):
        R, F, E = 1.0, 2.0, 3.0
        result = self.harmonic_balancer.apply_golden_harmony(R, F, E)
        expected = np.sqrt((R * F**2) + E**2)
        self.assertAlmostEqual(result, expected)

    def test_apply_resonance_condition(self):
        F0, k, m, omega, b = 1.0, 2.0, 3.0, 4.0, 5.0
        result = self.harmonic_balancer.apply_resonance_condition(F0, k, m, omega, b)
        expected = F0 / np.sqrt((k - m * omega**2)**2 + (b * omega)**2)
        self.assertAlmostEqual(result, expected)

    def test_apply_wave_interference(self):
        y1, y2 = 1.0, 2.0
        result = self.harmonic_balancer.apply_wave_interference(y1, y2)
        expected = y1 + y2
        self.assertAlmostEqual(result, expected)

if __name__ == "__main__":
    unittest.main()