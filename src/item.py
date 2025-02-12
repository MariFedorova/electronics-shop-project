import csv

from abc import ABC, abstractmethod


class InstantiateCSVError(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        # self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[0:10]

    @classmethod
    def instantiate_from_csv(cls, filename):
        try:
            with open(filename, "r", encoding="Windows-1251") as file:
                reader = csv.DictReader(file, delimiter=',')
                for row in reader:
                    if len(row) != 3:
                        raise InstantiateCSVError("Файл item.csv поврежден")
                    new_item = cls(row.get('name'), int(row.get('price')), int(row.get('quantity')))
                    cls.all.append(new_item)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(data):
        return int(float(data))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

# class Keybord():
