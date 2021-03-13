from typing import List, Tuple

import numpy as np


class NeuralNetwork:
    def __init__(self, hidden_sizes: List[int], output_size: int, input_size: int) -> None:
        self.weights = []  # inicjujemy wagi sieci dla warstw ukrytych
        self.layers = []  # umieszczamy wartosci znajdujace sie w poszczegolnych ukrytych warstwach sieci

    def predict(self, input_: np.ndarray) -> np.ndarray:
        # zwracamy wartosci znajdujace sie w ostatniej warstwie sieci
        pass

    def fit(self, data: np.ndarray, labels: np.ndarray, iterations: int, alpha: float) -> float:
        # zwracamy wartosc bledu treningu
        pass
