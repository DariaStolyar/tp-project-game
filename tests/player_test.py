import warnings

from src.entities.player import Player

warnings.filterwarnings("ignore")


def test_player_get_pos() -> None:
    actor = Player((5, 5), "")
    assert (5, 5) == actor.get_position()


def test_player_set_pos() -> None:
    actor = Player((5, 5), "")
    actor.set_position((6, 6))
    assert (6, 6) == (actor.x, actor.y)
