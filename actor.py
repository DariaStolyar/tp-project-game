from abc import abstractmethod

import pygame
from play import Lab

from entity import Entity


class Actor(Entity):
    def __init__(self, position: tuple[int, int], png: str) -> None:
        self.x, self.y = position
        self.map = []
        self.h = len(self.map)
        self.w = len(self.map[0])
        self.tile_size = 40
        self.png = png

    def get_position(self) -> tuple[int, int]:
        return self.x, self.y

    def set_position(self, position: tuple[int, int]) -> None:
        self.x, self.y = position

    def render(self, screen: Surface) -> None:
        my_image = pygame.image.load(self.png).convert_alpha()
        scaled_image = pygame.transform.scale(my_image, (self.tile_size, self.tile_size))
        screen.blit(scaled_image, (self.x * self.tile_size, self.y * self.tile_size))

    @abstractmethod
    def update(self, lab: Lab, target: tuple[int, int] | None = None,
               time: float | None = None, speed: float | None = None) -> None:
        pass
