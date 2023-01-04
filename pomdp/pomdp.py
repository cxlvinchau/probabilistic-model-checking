import numpy as np

class State:

    def __init__(self, obs: np.ndarray):
        self.obs = obs


class Transition:

    def __init__(self, source, action, target, prob, reward):
        self.source = source
        self.action = action
        self.target = ta
