"""Refactored retail system for Task 1.

The Payment component was redesigned to use a dictionary-based dispatch
approach instead of separate payment strategy classes.
"""


class Cart:
    """Stores items currently placed in a shopping cart."""

    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))
        print(f"Added {quantity} {item}(s) to the cart.")


class CartFactory:
    """Creates Cart objects."""

    @staticmethod
    def create_cart():
        return Cart()


class InventoryObserver:
    """Receives a message when inventory changes."""

    def notify(self, item, quantity):
        print(f"Notification: {item} stock is now {quantity}.")


class Inventory:
    """Stores stock and notifies registered observers."""

    def __init__(self):
        self.stock = {}
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def add_item(self, item, quantity):
        self.stock[item] = self.stock.get(item, 0) + quantity
        self.notify_observers(item)

    def notify_observers(self, item):
        for observer in self.observers:
            observer.notify(item, self.stock[item])


class PaymentProcessor:
    """Processes payments using a dictionary-based payment registry."""

    PAYMENT_METHODS = {
        "credit_card": "Credit Card",
        "paypal": "PayPal",
    }

    def process_payment(self, amount, method):
        # Validate the payment before processing it.
        if amount <= 0:
            print("Payment failed: the amount must be greater than zero.")
            return False

        # Use the registry to check whether the payment method is supported.
        method_name = self.PAYMENT_METHODS.get(method)

        if method_name is None:
            print(f"Payment failed: unsupported method '{method}'.")
            return False

        # The dictionary replaces the separate strategy classes used
        # in the starter program.
        print(f"Processing {amount} via {method_name}.")
        return True


class RetailSystem:
    """Combines the cart, inventory, and payment components."""

    def __init__(self):
        self.cart = CartFactory.create_cart()
        self.payment_processor = PaymentProcessor()
        self.inventory = Inventory()

    def add_item_to_inventory(self, item, quantity):
        self.inventory.add_item(item, quantity)

    def add_item_to_cart(self, item, quantity):
        if self.inventory.stock.get(item, 0) >= quantity:
            self.cart.add_item(item, quantity)
            self.inventory.stock[item] -= quantity
        else:
            print(f"Not enough stock for {item}.")

    def checkout(self, amount, method):
        return self.payment_processor.process_payment(amount, method)


if __name__ == "__main__":
    retail_system = RetailSystem()

    retail_system.add_item_to_inventory("Laptop", 5)
    retail_system.add_item_to_inventory("Phone", 10)

    retail_system.add_item_to_cart("Laptop", 2)
    retail_system.add_item_to_cart("Phone", 1)

    retail_system.checkout(1500, "credit_card")