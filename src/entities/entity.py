from abc import abstractmethod

import pygame


class Entity:
    @abstractmethod
    def __init__(self, position: tuple[int, int], png: str | None = None) -> None:
        pass

    @abstractmethod
    def render(self, screen: pygame.Surface) -> None:
        pass
