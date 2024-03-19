import pygame
from play import Lab

from actor import Actor


class Player(Actor):
    def update(self, lab: Lab) -> None:
        n_x, n_y = self.get_position()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            n_x -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            n_x += 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            n_y += 1
        if pygame.key.get_pressed()[pygame.K_UP]:
            n_y -= 1
        if lab.is_free((n_x, n_y)):
            self.set_position((n_x, n_y))
