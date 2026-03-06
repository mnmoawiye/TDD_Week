def add_item(inventory, item):
    if inventory["locked"]:
        return inventory  
    if not isinstance(item, str) or item == "":
        raise ValueError("Item must be a non-empty string")
    if len(inventory["items"]) >= inventory["capacity"]:
        raise ValueError("Inventory is full")
    inventory["items"].append(item)
    return inventory


def remove_item(inventory, item):
    if inventory["locked"]:
        return inventory
    if item not in inventory["items"]:
        raise ValueError("Item not found in inventory")
    inventory["items"].remove(item)
    return inventory


def get_item_count(inventory):
    return len(inventory["items"])