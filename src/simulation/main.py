import numpy as np
from . import ParameterEstimationModel, CurrentAmplitudeAdaptiveFilter, ActivationLevelModel
from . import StimulationSystem


# Stimulation System Controller

# Mock Models for Demonstration
class MockModel:
    def predict(self, input_data):
        # This is a mock prediction function
        return input_data * 0.8 + 0.2

# Example Usage
if __name__ == "__main__":
    # Instantiate mock models and the LMS filter
    current_estimator = ParameterEstimationModel(MockModel())
    adaptive_filter = CurrentAmplitudeAdaptiveFilter(num_parameters=1, learning_rate=0.01)
    activation_level_estimator = ActivationLevelModel(MockModel())
    
    # Instantiate the stimulation system controller
    system = StimulationSystem(current_estimator, adaptive_filter, activation_level_estimator)
    
    # Desired activation level (this is what you want to achieve)
    desired_activation_level = 1.0
    
    # Run the system for a few iterations to observe the adaptation
    for iteration in range(10):
        applied_current, actual_activation_level, error = system.run_iteration(desired_activation_level)
        print(f"Iteration {iteration+1}:")
        print(f"  Applied Current: {applied_current}")
        print(f"  Actual Activation Level: {actual_activation_level}")
        print(f"  Error: {error}")
