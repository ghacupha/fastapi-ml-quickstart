import joblib
import numpy as np
from pathlib import Path

from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston


class Model:
    """
    Models Definition.
        
        This is a general representation of what we do with a model that we are serving, henceforth
        applied as the matrix throughout the application
    """

    def __init__(self, model_path: str = None):
        self._model = None
        self._model_path = model_path
        self.load()

    def train(self, X: np.ndarray, y: np.ndarray):
        """
        Model definition and training.

           This method creates a model using the underlying library implementation, the data
           provided in the feature matrix X, is related to the data in the matrix y
        """
        self._model = RandomForestRegressor()
        self._model.fit(X, y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Prediction logic.

           Returns array with predictions corresponding to the input matrix X
        """
        return self._model.predict(X)

    def save(self):
        """
        Model persistence to the file system.

        This method saves the model to the path provided when creating the model object; internally the
        implementation uses joblib
        """
        if self._model is not None:
            joblib.dump(self._model, self._model_path)
        else:
            raise TypeError("The model is not trained yet, use .train() before saving")

    def load(self):
        """
        Load model from file system.

        This method creates the persistent, trained model as saved in the file system using joblib. It is
        important for consistency to use the same version of joblib when saving the model and when loading it
        """
        try:
            self._model = joblib.load(self._model_path)
        except:
            self._model = None
        return self


model_path = Path(__file__).parent / "model.joblib"
n_features = load_boston(return_X_y=True)[0].shape[1]
model = Model(model_path)


def get_model():
    """
    Model singleton.

    This function returns the model to be used through out the application. The model is already 
    configured and trained and is ready for use in prediction. The same is loaded from the file
    system model.joblib file
    """

    return model


if __name__ == "__main__":
    X, y = load_boston(return_X_y=True)
    model.train(X, y)
    model.save()
