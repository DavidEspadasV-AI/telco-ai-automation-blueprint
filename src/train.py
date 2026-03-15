from simulator import TelcoDigitalTwin
from optimizer import NetworkAIOptimizer

def run_automation_loop(episodes=10):
    twin = TelcoDigitalTwin()
    ai_engine = NetworkAIOptimizer()
    
    print(f"--- Starting Network Autonomous Loop ---")
    for i in range(episodes):
        metrics = twin.get_metrics()
        action = ai_engine.compute_action(metrics)
        new_metrics = twin.apply_optimization(action)
        
        print(f"Episode {i+1}: Latency Improved to {new_metrics['avg_latency']:.4f}")

if __name__ == "__main__":
    run_automation_loop()