import abc


class Soda:

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


class SodaMachine:
    pass

    def start(self):
        pass


if __name__ == "__main__":
    machine = SodaMachine()
    machine.start()