"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def test_item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(test_item):
    test_item.calculate_total_price()
    assert test_item.price * test_item.quantity == 200000


def test_apply_discount(test_item):
    test_item.apply_discount()
    assert test_item.price == 8000


def test_string_to_number():
    assert Item.string_to_number('5.0') == 5


def test_name(test_item):
    test_item.name = 'СуперСмартфон'
    assert test_item.name == 'СуперСмарт'


def test_repr(test_item):
    assert repr(test_item) == "Item('Смартфон', 10000, 20)"


def test_str(test_item):
    assert str(test_item) == 'Смартфон'
