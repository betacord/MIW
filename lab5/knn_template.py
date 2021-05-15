from typing import Any, Callable

import numpy as np


class DecisionSystem:
    __objects: np.ndarray
    __decisions: np.ndarray

    def __init__(self, filename: str) -> None:
        pass  # wczytuje dane z pliku do zbioru obiektow i decyzji

    def get_object(self, i: int) -> np.ndarray:
        pass  # zwraca obiekt o i-tym indeksie

    def get_decision(self, i: int) -> np.ndarray:
        pass  # zwraca decyzje dla obiektu o i-tym indeksie

    def __len__(self) -> int:
        pass  # zwraca liczbe obiektow w systemie decyzyjnym


class Knn:
    __decision_system: DecisionSystem

    def __init__(self, decision_system: DecisionSystem) -> None:
        pass  # przekazuje do instancji system decyzyjny

    def predict(self, obj: np.ndarray, k: int, metric: Callable[[np.ndarray], float]) -> Any:
        pass  # zwraca przydzielona decyzje

    def __find_closest_objects(self, obj: np.ndarray, k: int,
                               metric: Callable[[np.ndarray, np.ndarray], float]) -> np.ndarray:
        pass  # zwraca k najblizszych obiektow
