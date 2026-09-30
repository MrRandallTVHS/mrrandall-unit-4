"""Inventory service for Task 2."""


def update_stock(inventory, item, quantity):
    """Add stock to an item and return a success or error result."""

    # The service validates its own input.
    if not isinstance(quantity, int) or quantity <= 0:
        return {
            "error": "Quantity must be a positive whole number."
        }

    if not item:
        return {
            "error": "An item name is required."
        }

    # The Inventory service owns the stock update logic.
    inventory[item] = inventory.get(item, 0) + quantity

    return {
        "message": f"{item} stock updated.",
        "stock": inventory[item]
    }