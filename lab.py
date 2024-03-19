from pygame import Surface


class Lab:
    def __init__(self, filename: str, finish_t: tuple[int, int]) -> None:
        pass

    def render(self, screen: Surface):
        pass

    def get_tile_id(self, position: tuple[int, int]) -> int:
        pass

    def is_free(self, position: tuple[int, int]) -> bool:
        pass
