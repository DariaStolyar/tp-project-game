from abc import abstractmethod

from pygame import Surface


class Entity:
    @abstractmethod
    def __init__(self, position: tuple[int, int], png: str | None = None) -> None:
        pass

    @abstractmethod
    def render(self, screen: Surface) -> none:
        pass
