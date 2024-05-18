import warnings

import pytest

from src.entities.enemy import Enemy
from src.lab import Lab

warnings.filterwarnings("ignore")


@pytest.mark.parametrize('time,expected', [(7, (6, 5)), (6, (5, 5))])
def test_enemy_update(time: int, expected: tuple[int, int]) -> None:
    lab = Lab('uo.txt')
    enemy = Enemy((5, 5), "")
    enemy.update(lab, (6, 5), time)
    assert expected == (enemy.x, enemy.y)


@pytest.mark.parametrize('target,expected', [((10, 5), (6, 5)), ((5, 5), (5, 5))])
def test_enemy_find_step(target: tuple[int, int], expected: tuple[int, int]) -> None:
    lab = Lab('uo.txt')
    enemy = Enemy((5, 5), "")
    assert expected == enemy.find_step(target, lab)
