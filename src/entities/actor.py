from abc import abstractmethod

import pygame

from src.entities.entity import Entity
from src.lab import Lab


class Actor(Entity):
    def __init__(self, position: tuple[int, int], png: str) -> None:
        self.x, self.y = position
        self.tile_size = 40
        self.png = png

    def get_position(self) -> tuple[int, int]:
        return self.x, self.y

    def set_position(self, position: tuple[int, int]) -> None:
        self.x, self.y = position

    def render(self, screen: pygame.Surface) -> None:
        my_image = pygame.image.load(self.png).convert_alpha()
        scaled_image = pygame.transform.scale(my_image, (self.tile_size, self.tile_size))
        screen.blit(scaled_image, (self.x * self.tile_size, self.y * self.tile_size))

    @abstractmethod
    def update(self, lab: Lab, target: tuple[int, int], time: int | None, speed: int | None) -> None:
        pass
