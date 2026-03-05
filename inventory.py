def add_item(inventory, item):
    inventory.append(item)
    return inventory

def remove_item(inventory, item):
    if item in inventory:
        inventory.remove(item)
    return inventory

def get_item_count(inventory):
    return len(inventory)