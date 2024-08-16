from .parameter_estimation_model import ParameterEstimationModel
from .activation_level_model import ActivationLevelModel
from .parameter_adaptive_filter import CurrentAmplitudeAdaptiveFilter
from .sim import StimulationSystem

class NeuralNetworkModel:
    def predict(self, input_data):
        raise NotImplementedError("This method should be overridden by subclasses")

class AdaptiveFilter:
    def update(self, input_data, desired_output):
        raise NotImplementedError("This method should be overridden by subclasses")