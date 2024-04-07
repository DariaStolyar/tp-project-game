import pygame

from src.entities.actor import Actor
from src.lab import Lab


class Player(Actor):
    def update(self, lab: Lab, keys_list: dict[str, int], target: tuple[int, int] | None = None,
               time: int | None = None, speed: int | None = None) -> None:
        n_x, n_y = self.get_position()
        if pygame.key.get_pressed()[keys_list['LEFT']]:
            n_x -= 1
        elif pygame.key.get_pressed()[keys_list['RIGHT']]:
            n_x += 1
        elif pygame.key.get_pressed()[keys_list['DOWN']]:
            n_y += 1
        elif pygame.key.get_pressed()[keys_list['UP']]:
            n_y -= 1
        if lab.is_free((n_x, n_y)):
            self.set_position((n_x, n_y))
