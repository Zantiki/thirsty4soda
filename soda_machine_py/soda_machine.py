import abc
import re
import string
from enum import Enum
from time import sleep
from typing import Dict


class Soda:

    @classmethod
    @property
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
    sms_order = "sms order"
    recall = "recall"
    kill = "kill"


class SodaFactory:
    _types = {
        Coke.name: Coke(),
        Sprite.name: Sprite(),
        Fanta.name: Fanta()
    }

    @staticmethod
    def get_by_name(soda_name: str):
        return SodaFactory._types[soda_name]


class SodaMachine:

    def __init__(self, inventory: Dict[str, int] = None):
        if not inventory:
            inventory = SodaMachine.get_default_inventory()

        self.inventory = inventory
        self._internal_cash = 0
        self.kill = False

    @staticmethod
    def get_default_inventory():
        default_inventory = {
            Coke.name: 5,
            Sprite.name: 3,
            Fanta.name: 3
        }
        return default_inventory

    def get_sodas_available(self):
        return [soda for soda in self.inventory.keys()]

    def show_instructions(self):
        instructions = (f"Available Commands: \n"
                        f"{SodaActions.insert.value} (money) - put money into money slot\n"
                        f"{SodaActions.order.value} ({', '.join(self.get_sodas_available())}) - order from machine buttons\n"
                        f"{SodaActions.sms_order.value} ({', '.join(self.get_sodas_available())}) - order sent by sms\n"
                        f"{SodaActions.recall.value} - gives the money back")
        print(instructions)

    def show_balance(self):
        balance_info = f"Money available {self._internal_cash}"
        wrap_string = "-" * 7
        print(f"{wrap_string}\n{balance_info}\n{wrap_string}")

    def handle_soda_order(self, action_input: str):
        assert action_input in self.get_sodas_available(), f"Cannot understand order {action_input}"
        number_of_sodas = self.inventory[action_input]
        soda = SodaFactory.get_by_name(action_input)
        assert number_of_sodas > 0, f"Out of item {action_input}"
        assert self._internal_cash >= soda.price, f"You cannot afford {action_input}"
        print(f"Giving out {soda.name}")
        self.inventory[action_input] -= 1
        self.subtract_from_cash(soda.price)
        if self._internal_cash:
            self.return_cash()

    def subtract_from_cash(self, number: float):
        self._internal_cash -= number

    def return_cash(self):
        print(f"Returning {self._internal_cash}")
        self.subtract_from_cash(self._internal_cash)

    def handle_cash_order(self, action_input: str):
        number_value = float(action_input)
        self._internal_cash += number_value
        print(f"Added {action_input}")

    def handle_order(self, action: str, action_input: str):
        if action == SodaActions.order.value or action == SodaActions.sms_order.value:
            self.handle_soda_order(action_input)

        if action == SodaActions.insert.value:
            self.handle_cash_order(action_input)

        if action == SodaActions.recall.value:
            self.return_cash()

        if action == SodaActions.kill.value:
            self.kill = True

    def handle_user_input(self):
        action_values = [action.value for action in SodaActions]
        action_input_regex = fr"({'|'.join(action_values)})(.*)"
        user_input = input("What do you want to do?: ")
        try:
            input_match = re.match(action_input_regex, user_input)
            action = input_match.group(1)
            action_input = input_match.group(2)
            self.handle_order(action, action_input.replace(" ", ""))
        except Exception as e:
            print(f"Problems with input: {e}")
        print(f"Balance is {self._internal_cash}\n\n")
        # For a bit of feedback before resetting
        sleep(3)

    def start(self):

        while not self.kill:
            self.show_instructions()
            self.show_balance()
            self.handle_user_input()


if __name__ == "__main__":
    machine = SodaMachine()
    machine.start()