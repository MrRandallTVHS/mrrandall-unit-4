"""Orchestrator for the Inventory service."""

# The orchestrator coordinates the test but does not contain
# the inventory service's business logic.

from inventory_service import update_stock


def run_tests():
    """Run one successful and one invalid Inventory operation."""

    # This test provides valid input and should update the stock.

    print("Successful operation:")

    inventory = {"Laptop": 5}
    successful_result = update_stock(inventory, "Laptop", 5)

    print(successful_result)
    print(f"Inventory after update: {inventory}")
    print()

    # This test provides an invalid negative quantity.
    # The service should reject it and leave the inventory unchanged.

    print("Unsuccessful or invalid operation:")

    invalid_inventory = {"Laptop": 5}
    invalid_result = update_stock(invalid_inventory, "Laptop", -2)

    print(invalid_result)
    print(f"Inventory after invalid update: {invalid_inventory}")


if __name__ == "__main__":
    run_tests()