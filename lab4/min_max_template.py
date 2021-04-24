from typing import Any, List, Callable, Optional


class TreeNode:
    """
    klasa reprezntujaca wezel grafu gry
    value: wartosc odpowiadajaca biezacemu graczowi (antagonista/protagonista)
    state: wartosc odpowiadajaca dokonanemu ruchowi
    score: wartosc odpowiadajaca wynikowi w biezacym stanie
    children: lista obiektow wszystkich wezlow potomnych
    """

    value: Any
    state: Optional[Any]
    score: Optional[int]
    children: List['TreeNode']

    def __init__(self, value: Any, state: Optional[Any] = None, score: Optional[int] = 0) -> None:
        self.value = value
        self.state = state
        self.score = score
        self.children = []

    @property
    def is_leaf(self) -> bool:
        pass  # zwracamy True jezeli biezacy wezel jest lisciem lub False

    def add(self, child: 'TreeNode') -> None:
        pass  # dodajemy nowy wezel potomny

    def traverse_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        pass  # odwiedzamy rekurencyjnie wszystkie wezly potomne, na koncu korzen


class Tree:
    """
    klasa reprezentujaca graf gry (drzewo)
    root: referencja do korzenia drzewa
    """

    root: TreeNode

    def __init__(self, node: TreeNode) -> None:
        self.root = node

    def min_max(self) -> None:
        pass  # wykonujemy rekurencyjnie metode min-max dla wszystkich wezlow potomnych

    def show(self) -> None:
        pass  # wizualizujemy wszystkie wezly grafu gry wraz z krawedziami

    def __traverse_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        pass  # odwiedzamy rekurencyjnie wszystkie wezly potomne korzenia
