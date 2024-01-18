import abc
import string
from enum import Enum
from typing import Dict


class Soda:

    @property
    @classmethod
    def name(cls):
        return cls.__name__.lower()

    @property
    @abc.abstractmethod
    def price(self):
        pass


class Coke(Soda):
    price = 20.00


class Fanta(Soda):
    price = 15.00


class Sprite(Soda):
    price = 15.00


class SodaActions(Enum):
    insert = "insert"
    order = "order"
    sms_order = "sms_order"
    recall = "recall"


class SodaMachine:

    def __init__(self, inventory: Dict[string, int]):
        if not inventory:
            inventory = SodaMachine.get_default_inventory()

        self.inventory = inventory
        self.internal_cash = 0
        self.kill = False

    @staticmethod
    def get_default_inventory():
        default_inventory = {
            Coke.name: 5,
            Sprite.name: 3,
            Fanta.name: 3
        }
        return default_inventory

    def show_instructions(self):
        pass

    def start(self):

        while not self.kill:
            pass



if __name__ == "__main__":
    machine = SodaMachine()
    machine.start()