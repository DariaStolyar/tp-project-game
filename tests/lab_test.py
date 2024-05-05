import warnings

import pytest

from src.lab import Lab

warnings.filterwarnings("ignore")


@pytest.mark.parametrize('x,y,expected', [(5, 5, 0), (4, 4, 1),
                                          (0, 21, 2), (19, 9, 3)])
def test_actor(x: int, y: int, expected: int) -> None:
    lab = Lab('uo.txt')
    assert expected == lab.get_tile_id((x, y))


@pytest.mark.parametrize('x,y,expected', [(5, 5, True), (4, 4, False),
                                          (0, 21, False), (19, 9, True)])
def test_is_free(x: int, y: int, expected: bool) -> None:
    lab = Lab('uo.txt')
    assert expected == lab.is_free((x, y))
