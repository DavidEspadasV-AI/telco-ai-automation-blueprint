import numpy as np

class TelcoDigitalTwin:
    \"\"\"
    A simulated environment representing a 5G/6G network slice.
    It models traffic load, latency, and energy consumption.
    \"\"\"
    def __init__(self, num_nodes=5):
        self.num_nodes = num_nodes
        self.state = np.random.rand(num_nodes, 3) # Load, Latency, Energy
        
    def get_metrics(self):
        return {
            "avg_load": np.mean(self.state[:, 0]),
            "avg_latency": np.mean(self.state[:, 1]),
            "total_energy": np.sum(self.state[:, 2])
        }

    def apply_optimization(self, configuration):
        \"\"\"
        Adjusts network parameters based on AI configurations.
        configuration: array of parameter adjustments.
        \"\"\"
        # Simulated impact of AI optimization on network state
        noise = np.random.normal(0, 0.05, self.state.shape)
        self.state = np.clip(self.state - configuration + noise, 0, 1)
        return self.get_metrics()