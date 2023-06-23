"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)


    item1.calculate_total_price()
    assert item1.price * item1.quantity == 200000
    assert item2.price * item2.quantity == 100000

    # устанавливаем новый уровень цен

    # применяем скидку
def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)

    item1.apply_discount()

    assert item1.price == 8000.0


