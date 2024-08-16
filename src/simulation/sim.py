import numpy as np

class StimulationSystem:
    def __init__(self, current_estimator, adaptive_filter, activation_level_estimator):
        self.current_estimator = current_estimator
        self.adaptive_filter = adaptive_filter
        self.activation_level_estimator = activation_level_estimator
    
    def run_iteration(self, desired_activation_level):
        # Step 1: Estimate required current amplitude using neural network model
        estimated_current = self.current_estimator.predict(desired_activation_level)
        
        # Step 2: Pass the current estimate through the adaptive filter
        _, filtered_current = self.adaptive_filter.update(np.array([1]), estimated_current)  # Single parameter for simplicity
        
        # Step 3: Apply the current in the stimulation (this is usually hardware interfacing)
        applied_current = filtered_current
        
        # Step 4: Determine the actual activation level using the neural network model
        actual_activation_level = self.activation_level_estimator.predict(applied_current)
        
        # Step 5: Feed the actual activation level into the adaptive filter to update the current amplitude
        error, _ = self.adaptive_filter.update(np.array([1]), actual_activation_level)
        
        return applied_current, actual_activation_level, error