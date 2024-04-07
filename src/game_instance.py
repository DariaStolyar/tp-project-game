import pygame

from src.entities.actor import Actor
from src.entities.coin import Coin
from src.lab import Lab


class GameInstance:
    def __init__(self, mode_is_single: bool, lab: Lab, actor1: Actor, actor2: Actor, coins: list[Coin]) -> None:
        self.mode_is_single = mode_is_single
        self.lab = lab
        self.actor1 = actor1
        self.actor2 = actor2
        self.coins = coins

    def render(self, screen: pygame.Surface) -> None:
        self.lab.render(screen)
        for i in self.coins:
            i.render(screen)
        self.actor1.render(screen)
        self.actor2.render(screen)
