import numpy as np


class MockModel:
    """
    Mock implementation of the Model
    """
    def __init__(self, model_path: str = None):
        self._model_path = None
        self._model = None

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Fake prediction logic.

        This method returns an array with fake predictions for the X matrix, by merely returning
        random numbers in an array whose dimensions match the y matrix (number of rows of X matrix)
        """
        n_instances = len(X)
        return np.random.rand(n_instances)

    def train(self, X: np.ndarray, y: np.ndarray):
        """
        Return an instance of this model
        """
        return self

    def save(self):
        """
        Save method blank as it's merely for training purposes
        """

    def load(self):
        """
        Return an instance of this model
        """
        return self
