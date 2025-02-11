"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_str(item1):
    assert str(item1) == 'Смартфон'


def test_repr(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_item_init(item1):
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    assert item1.apply_discount() == 10000
