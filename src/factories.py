from abc import abstractmethod

from src.entities.actor import Actor
from src.entities.coin import Coin, YellowCoin, BlueCoin, GreenCoin
from src.entities.enemy import Enemy
from src.entities.entity import Entity
from src.entities.player import Player


class EntityFactory:
    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    def create(position: tuple[int, int], png: str | None = None) -> Entity:
        pass


class CoinFactory(EntityFactory):
    @staticmethod
    @abstractmethod
    def create(position: tuple[int, int], png: str | None = None) -> Coin:
        pass


class YellowCoinFactory(CoinFactory):
    @staticmethod
    def create(position: tuple[int, int], png: str | None = None) -> YellowCoin:
        return YellowCoin(position)


class BlueCoinFactory(CoinFactory):
    @staticmethod
    def create(position: tuple[int, int], png: str | None = None) -> BlueCoin:
        return BlueCoin(position)


class GreenCoinFactory(CoinFactory):
    @staticmethod
    def create(position: tuple[int, int], png: str | None = None) -> GreenCoin:
        return GreenCoin(position)


class ActorFactory(EntityFactory):
    @staticmethod
    @abstractmethod
    def create(position: tuple[int, int], png: str | None = None) -> Actor:
        pass


class PlayerFactory(ActorFactory):
    @staticmethod
    def create(position: tuple[int, int], png: str | None = None) -> Player:
        return Player(position, png)


class EnemyFactory(ActorFactory):
    @staticmethod
    def create(position: tuple[int, int], png: str | None = None) -> Enemy:
        return Enemy(position, png)
