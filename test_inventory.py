import pytest
from inventory import add_item, remove_item, get_item_count

# add_item tests
def test_add_item_basic(empty_inventory):
    inv = add_item(empty_inventory, "sword")
    assert "sword" in inv["items"]

def test_add_item_locked(locked_inventory):
    inv = add_item(locked_inventory, "shield")
    assert inv == locked_inventory 

def test_add_item_invalid(empty_inventory):
    with pytest.raises(ValueError):
        add_item(empty_inventory, "") 

# remove_item tests 
def test_remove_item_basic(partially_filled_inventory):
    inv = remove_item(partially_filled_inventory, "potion")
    assert "potion" not in inv["items"]

def test_remove_item_not_found(empty_inventory):
    with pytest.raises(ValueError):
        remove_item(empty_inventory, "axe")

#get_item_count tests 
def test_get_item_count_basic(partially_filled_inventory):
    assert get_item_count(partially_filled_inventory) == 2

def test_get_item_count_empty(empty_inventory):
    assert get_item_count(empty_inventory) == 0