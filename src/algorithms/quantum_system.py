import numpy as np

class QuantumSystem:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.parameters = np.zeros(num_qubits)

    def evolve_state(self, state, steps=1):
        if not isinstance(state, np.ndarray) or state.shape != (self.num_qubits,):
            raise ValueError(f"Invalid state vector shape. Expected ({self.num_qubits},), got {state.shape}")
        for _ in range(steps):
            state = state * np.exp(-1j * self.parameters)
        return state / np.linalg.norm(state)

    def update_parameters(self, state, score, transition_constant):
        """
        Update the quantum system parameters based on the state and score.
        
        Args:
            state (list): The current state vector.
            score (float): The score associated with the state.
            transition_constant (float): The transition constant for updating parameters.
        """
        # Normalize the state vector
        normalized_state = np.array(state) / np.linalg.norm(state)
        
        # Update parameters based on the normalized state and score
        self.parameters += transition_constant * score * normalized_state

    def get_parameters(self):
        """
        Get the current parameters of the quantum system.
        
        Returns:
            np.ndarray: The current parameters.
        """
        return self.parameters

    def reset_parameters(self):
        """
        Reset the parameters of the quantum system to zero.
        """
        self.parameters = np.zeros(self.num_qubits)