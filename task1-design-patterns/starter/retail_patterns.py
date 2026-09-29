"""Starter code for Task 1.

The three components intentionally use different design patterns so that
students can identify, evaluate, and refactor them.
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


class PaymentStrategy:
    """Defines the operation expected from a payment strategy."""

    def pay(self, amount):
        raise NotImplementedError


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing {amount} via Credit Card.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing {amount} via PayPal.")


class PaymentProcessor:
    """Processes payment using the selected strategy."""

    def __init__(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


class RetailSystem:
    """Combines the cart, inventory, and payment components."""

    def __init__(self):
        self.cart = CartFactory.create_cart()
        self.payment_processor = PaymentProcessor(CreditCardPayment())
        self.inventory = Inventory()

    def add_item_to_inventory(self, item, quantity):
        self.inventory.add_item(item, quantity)

    def add_item_to_cart(self, item, quantity):
        if self.inventory.stock.get(item, 0) >= quantity:
            self.cart.add_item(item, quantity)
            self.inventory.stock[item] -= quantity
        else:
            print(f"Not enough stock for {item}.")

    def checkout(self, amount):
        self.payment_processor.process_payment(amount)


if __name__ == "__main__":
    retail_system = RetailSystem()
    retail_system.add_item_to_inventory("Laptop", 5)
    retail_system.add_item_to_inventory("Phone", 10)
    retail_system.add_item_to_cart("Laptop", 2)
    retail_system.add_item_to_cart("Phone", 1)
    retail_system.checkout(1500)

