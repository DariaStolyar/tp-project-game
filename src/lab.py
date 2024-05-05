import pygame

from src.globals import DATA, TILE_SIZE


class Lab:
    def __init__(self, filename: str) -> None:
        self.map = []
        with open(f"{DATA['maps_dir']}/{filename}") as input_file:
            for line in input_file:
                self.map.append(list(map(int, line.split())))
        self.h = len(self.map)
        self.w = len(self.map[0])

    def render(self, screen: pygame.Surface) -> None:
        colors = {0: (174, 96, 170), 1: (255, 0, 0), 2: (0, 0, 0), 3: (153, 153, 153)}
        for y in range(self.h):
            for x in range(self.w):
                if self.get_tile_id((x, y)) == 1:
                    a, b = TILE_SIZE, TILE_SIZE
                    pygame.draw.rect(screen, (123, 47, 139), (x * TILE_SIZE, y * TILE_SIZE, a, b))
                    for i in range(4, a + 2, 8):
                        for j in range(4, b + 2, 8):
                            pygame.draw.rect(screen, (14, 9, 15), (x * TILE_SIZE + a - i, y * TILE_SIZE + b - j, 4, 4))
                    for i in range(4, a + 2, 12):
                        for j in range(4, b + 2, 12):
                            pygame.draw.rect(screen, (201, 0, 190), (x * TILE_SIZE + a - i, y * TILE_SIZE + b - j, 4, 4))
                    for i in range(4, a + 2, 10):
                        for j in range(4, b + 2, 10):
                            pygame.draw.rect(screen, (153, 153, 153), (x * TILE_SIZE + a - i, y * TILE_SIZE + b - j, 4, 4))
                else:
                    rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    screen.fill(colors[self.get_tile_id((x, y))], rect)

    def get_tile_id(self, position: tuple[int, int]) -> int:
        return self.map[position[1]][position[0]]

    def is_free(self, position: tuple[int, int]) -> bool:
        return self.get_tile_id(position) in [0, 3]
