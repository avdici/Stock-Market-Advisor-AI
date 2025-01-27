import torch

class Standarize:
    def __init__(self, keys=['Volume']):
        """
        Args:
            - mean: mean of feature over time series
            - std: std of feature over time series
            - keys: specified features to standarize
        """

        self.keys = keys

    def __call__(self, sample):
        for key in sample.keys():
            if key in self.keys:
                sample[key] = (sample[key] - sample['mean'][key]) / sample['std'][key]

        return sample
    
class MinMaxNorm:
    def __init__(self, min=0, max=1, keys=['Open', 'High', 'Low', 'Close']):
        """
        Args:
            - min: min of feature over time series
            - max: max of feature over time series
            - keys: specified features to min max scale
        """

        self.min = min
        self.max = max
        self.keys = keys

    def __call__(self, sample):
        for key in sample.keys():
            if key in self.keys:
                sample[key] = ((sample[key] - sample['min'][key]) / (sample['max'][key] - sample['min'][key])) \
                * (self.max - self.min) + self.min
    
        return sample