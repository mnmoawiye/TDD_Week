import pytest
from inventory import add_item, remove_item, get_item_count


def test_add_item_basic():
    inv = []
    result = add_item(inv, "sword")
    assert "sword" in result


def test_remove_item_basic():
    inv = ["sword", "shield"]
    result = remove_item(inv, "sword")
    assert "sword" not in result


def test_get_item_count_basic():
    inv = ["sword", "shield", "potion"]
    assert get_item_count(inv) == 3