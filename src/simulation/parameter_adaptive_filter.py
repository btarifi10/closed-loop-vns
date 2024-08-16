import numpy as np

from . import AdaptiveFilter


class CurrentAmplitudeAdaptiveFilter(AdaptiveFilter):
    def __init__(self, num_parameters, learning_rate=0.001):
        self.weights = np.ones(num_parameters)
        self.learning_rate = learning_rate
    
    def update(self, input_current, error):
        self.weights += self.learning_rate * error

        output = np.dot(self.weights, input_current)

        return output