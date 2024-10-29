import numpy as np # type: ignore
import time
import threading
import psutil # type: ignore
import matplotlib.pyplot as plt # type: ignore
from scipy.optimize import rosen # type: ignore
import json

class DeepResonanceLearning:
    def __init__(self, use_ght=True, cpu_threshold=70, energy_threshold=20, min_idle_time=2, max_iterations_per_cycle=5, history_size=10000):
        self.use_ght = use_ght
        self.cpu_threshold = cpu_threshold
        self.energy_threshold = energy_threshold
        self.min_idle_time = min_idle_time
        self.max_iterations_per_cycle = max_iterations_per_cycle
        self.history_size = history_size
        self.is_learning = False
        self.iterations_completed = 0
        self.learning_history = []
        self.model = np.random.rand(2)  # 2D Rosenbrock function
        self.harmony_memory = np.random.rand(10, 2)  # 10 harmony vectors of size 2
        self.PHI = (1 + np.sqrt(5)) / 2  # Golden Ratio
        self.best_solution = None
        self.best_score = float('inf')
        self.vibration_state = 1.0

    def start_learning(self):
        self.is_learning = True
        while self.is_learning:
            if self.should_perform_learning():
                self.perform_learning_cycle()
            else:
                time.sleep(self.min_idle_time)

    def stop_learning(self):
        self.is_learning = False

    def should_perform_learning(self):
        current_cpu = self.get_current_cpu_usage()
        current_energy = self.get_current_energy_consumption()
        return current_cpu < self.cpu_threshold and current_energy < self.energy_threshold

    def perform_learning_cycle(self):
        for _ in range(self.max_iterations_per_cycle):
            if not self.is_learning:
                break
            self.perform_single_iteration()
            self.iterations_completed += 1
        self.vibration_state = self.model.hermetic_principles.apply_vibration(self.vibration_state)
        # Use vibration_state to influence learning process

    def perform_single_iteration(self):
        if self.use_ght:
            new_harmony = self.generate_harmony_vector()
        else:
            new_harmony = np.random.rand(2)
        
        new_score = self.objective_function(new_harmony)
        if new_score < self.objective_function(self.model):
            self.model = new_harmony
        if new_score < self.best_score:
            self.best_solution = new_harmony
            self.best_score = new_score
        
        if self.use_ght:
            self.update_harmony_memory(new_harmony)
        
        time.sleep(0.01)  # Reduced simulation time for faster execution
        self.update_learning_history()

    def generate_harmony_vector(self):
        new_vector = np.zeros(2)
        for i in range(2):
            if np.random.rand() < 0.9:  # HARMONY_MEMORY_CONSIDERING_RATE
                j = np.random.randint(10)  # HARMONY_MEMORY_SIZE
                new_vector[i] = self.harmony_memory[j, i]
                if np.random.rand() < 0.1:  # PITCH_ADJUSTING_RATE
                    new_vector[i] += (np.random.rand() - 0.5) * 0.1  # Small adjustment
            else:
                new_vector[i] = np.random.rand()
        
        # Apply Golden Harmonic Sequence
        K = self.PHI * self.harmonic_mean(new_vector[0], new_vector[1])
        new_vector = K * new_vector
        
        return new_vector

    def harmonic_mean(self, a, b):
        return 2 * a * b / (a + b)

    def objective_function(self, model):
        return rosen(model)  # Rosenbrock function

    def update_harmony_memory(self, new_harmony):
        worst_index = np.argmax([self.objective_function(h) for h in self.harmony_memory])
        if self.objective_function(new_harmony) < self.objective_function(self.harmony_memory[worst_index]):
            self.harmony_memory[worst_index] = new_harmony

    def update_learning_history(self):
        self.learning_history.append({
            'timestamp': time.time(),
            'cpu_usage': self.get_current_cpu_usage(),
            'energy_consumption': self.get_current_energy_consumption(),
            'model_norm': np.linalg.norm(self.model),
            'best_score': self.best_score
        })
        if len(self.learning_history) > self.history_size:
            self.learning_history.pop(0)

    def get_current_cpu_usage(self):
        return psutil.cpu_percent(interval=0.1)

    def get_current_energy_consumption(self):
        return psutil.cpu_percent(interval=0.1) * 0.1  # Simulated energy consumption

    def get_learning_status(self):
        return {
            'is_learning': self.is_learning,
            'iterations_completed': self.iterations_completed,
            'current_cpu_usage': self.get_current_cpu_usage(),
            'current_energy_consumption': self.get_current_energy_consumption(),
            'learning_history': self.learning_history,
            'model_norm': np.linalg.norm(self.model),
            'best_score': self.best_score,
            'best_solution': self.best_solution
        }

    def perturb_model(self, magnitude):
        perturbation = np.random.randn(*self.model.shape) * magnitude
        self.model += perturbation
        self.update_learning_history()

def run_experiment(duration=7200, perturbations=None, use_ght=True):
    learner = DeepResonanceLearning(use_ght=use_ght)
    learning_thread = threading.Thread(target=learner.start_learning)
    learning_thread.start()
    
    start_time = time.time()
    while time.time() - start_time < duration:
        if perturbations:
            current_time = time.time() - start_time
            for t, magnitude in perturbations:
                if current_time >= t and current_time < t + 1:  # Apply perturbation for 1 second
                    learner.perturb_model(magnitude)
                    print(f"Applied perturbation of magnitude {magnitude} at time {current_time:.2f}")
        time.sleep(0.1)
    
    learner.stop_learning()
    learning_thread.join()
    
    return learner.get_learning_status()

def plot_results(ght_history, baseline_history, perturbations):
    ght_timestamps = [entry['timestamp'] for entry in ght_history]
    baseline_timestamps = [entry['timestamp'] for entry in baseline_history]
    ght_start_time = ght_timestamps[0]
    baseline_start_time = baseline_timestamps[0]
    ght_relative_times = [(t - ght_start_time) / 60 for t in ght_timestamps]  # Convert to minutes
    baseline_relative_times = [(t - baseline_start_time) / 60 for t in baseline_timestamps]  # Convert to minutes
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 24))
    
    # CPU Usage and Energy Consumption
    ax1.plot(ght_relative_times, [entry['cpu_usage'] for entry in ght_history], label='GHT CPU Usage')
    ax1.plot(ght_relative_times, [entry['energy_consumption'] * 10 for entry in ght_history], label='GHT Energy Consumption')
    ax1.plot(baseline_relative_times, [entry['cpu_usage'] for entry in baseline_history], label='Baseline CPU Usage')
    ax1.plot(baseline_relative_times, [entry['energy_consumption'] * 10 for entry in baseline_history], label='Baseline Energy Consumption')
    ax1.set_title('CPU Usage and Energy Consumption')
    ax1.set_xlabel('Time (minutes)')
    ax1.set_ylabel('Percentage / Arbitrary Units')
    ax1.legend()
    
    # Model Norm
    ax2.plot(ght_relative_times, [entry['model_norm'] for entry in ght_history], label='GHT')
    ax2.plot(baseline_relative_times, [entry['model_norm'] for entry in baseline_history], label='Baseline')
    ax2.set_title('Model Norm Over Time')
    ax2.set_xlabel('Time (minutes)')
    ax2.set_ylabel('Model Norm')
    ax2.legend()
    
    # Best Score (Rosenbrock function value)
    ax3.plot(ght_relative_times, [entry['best_score'] for entry in ght_history], label='GHT')
    ax3.plot(baseline_relative_times, [entry['best_score'] for entry in baseline_history], label='Baseline')
    ax3.set_title('Best Score Over Time (Rosenbrock function)')
    ax3.set_xlabel('Time (minutes)')
    ax3.set_ylabel('Best Score')
    ax3.set_yscale('log')  # Use log scale for better visualization
    ax3.legend()
    
    # Add vertical lines for perturbations
    for ax in [ax1, ax2, ax3]:
        for t, magnitude in perturbations:
            ax.axvline(x=t/60, color='r', linestyle='--', alpha=0.5)
            ax.text(t/60, ax.get_ylim()[1], f'P{magnitude}', rotation=90, verticalalignment='top')
    
    plt.tight_layout()
    plt.savefig('ght_vs_baseline_comparison.png')
    print("Results plot saved as ght_vs_baseline_comparison.png")

# Define perturbations: (time in seconds, magnitude)
perturbations = [
    (1800, 1.0),   # Minor perturbation at 30 minutes
    (3600, 5.0),   # Major perturbation at 60 minutes
    (5400, 2.5),   # Medium perturbation at 90 minutes
    (6300, 1.0),   # Minor perturbation at 105 minutes
]