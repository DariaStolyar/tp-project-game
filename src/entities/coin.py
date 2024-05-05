from abc import abstractmethod

import pygame

from src.entities.entity import Entity


class Coin(Entity):
    def __init__(self, position: tuple[int, int], png: str | None = None) -> None:
        self.position = self.x, self.y = position

    def get_position(self) -> tuple[int, int]:
        return self.x, self.y

    @abstractmethod
    def render(self, screen: pygame.Surface) -> None:
        pass


class YellowCoin(Coin):
    def render(self, screen: pygame.Surface) -> None:
        a, b = 20, 20
        x, y = self.x * 40 + 10, self.y * 40 + 10
        pygame.draw.rect(screen, (174, 96, 170), (x, y, a, b), 0)
        pygame.draw.circle(screen, (255, 220, 0), (x + a // 2, y + b // 2), a // 2)
        pygame.draw.circle(screen, (200, 200, 0), (x + a // 2, y + b // 2), a // 2, 3)
        pygame.draw.circle(screen, (255, 255, 0), (x + a // 2, y + b // 2), a // 2 - 15, 3)
        pygame.draw.polygon(screen, (250, 200, 0),
                                [(x + a // 2, y + 16), (x + 16, y + a // 2), (x + a // 2, y + a - 16),
                                 (x + a - 16, y + b // 2)])
        pygame.draw.circle(screen, (255, 255, 0), (x + a // 2, y + b // 2), a // 2 - 7, 0)


class GreenCoin(Coin):
    def render(self, screen: pygame.Surface) -> None:
        a, b = 20, 20
        x, y = self.x * 40 + 10, self.y * 40 + 10
        pygame.draw.rect(screen, (174, 96, 170), (x, y, a, b), 0)
        pygame.draw.circle(screen, (0, 220, 0), (x + a // 2, y + b // 2), a // 2)
        pygame.draw.circle(screen, (0, 200, 0), (x + a // 2, y + b // 2), a // 2, 3)
        pygame.draw.circle(screen, (0, 255, 0), (x + a // 2, y + b // 2), a // 2 - 15, 3)
        pygame.draw.polygon(screen, (0, 200, 0),
                            [(x + a // 2, y + 16), (x + 16, y + a // 2), (x + a // 2, y + a - 16),
                             (x + a - 16, y + b // 2)])
        pygame.draw.circle(screen, (0, 255, 0), (x + a // 2, y + b // 2), a // 2 - 7, 0)


class BlueCoin(Coin):
    def render(self, screen: pygame.Surface) -> None:
        a, b = 20, 20
        x, y = self.x * 40 + 10, self.y * 40 + 10
        pygame.draw.rect(screen, (174, 96, 170), (x, y, a, b), 0)
        pygame.draw.circle(screen, (0, 0, 100), (x + a // 2, y + b // 2), a // 2)
        pygame.draw.circle(screen, (0, 0, 200), (x + a // 2, y + b // 2), a // 2, 3)
        pygame.draw.circle(screen, (0, 0, 150), (x + a // 2, y + b // 2), a // 2 - 15, 3)
        pygame.draw.circle(screen, (0, 0, 240), (x + a // 2, y + b // 2), a // 2 - 7, 0)
