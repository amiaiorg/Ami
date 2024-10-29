import matplotlib.pyplot as plt # type: ignore

def plot_convergence(history):
    plt.plot(history['scores'])
    plt.title('Convergence of Harmonic Balancer Algorithm')
    plt.xlabel('Iteration')
    plt.ylabel('Best Score')
    plt.grid(True)
    plt.show()