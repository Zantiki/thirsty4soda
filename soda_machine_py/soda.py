import abc


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


class SodaFactory:
    _types = {
        Coke.name: Coke(),
        Sprite.name: Sprite(),
        Fanta.name: Fanta()
    }

    @staticmethod
    def get_by_name(soda_name: str):
        return SodaFactory._types[soda_name]

