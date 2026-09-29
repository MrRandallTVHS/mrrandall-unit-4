"""Starter monolithic retail system for Task 2.

Cart, inventory, and payment responsibilities are combined in one program.
Students will use this file to explain monolithic architecture and create
independent services.
"""


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append({"item": item, "quantity": quantity})
        return {"message": f"Added {quantity} {item}(s) to the cart."}


class Inventory:
    def __init__(self):
        self.stock = {}

    def update_stock(self, item, quantity):
        self.stock[item] = self.stock.get(item, 0) + quantity
        return {"message": f"{item} stock updated."}

    def get_stock(self, item):
        return {"item": item, "stock": self.stock.get(item, 0)}

    def remove_stock(self, item, quantity):
        current_stock = self.stock.get(item, 0)
        if current_stock < quantity:
            return {"error": f"Not enough stock for {item}."}
        self.stock[item] = current_stock - quantity
        return {"message": f"{quantity} {item}(s) removed from inventory."}


class Payment:
    def process_payment(self, amount, method):
        method_names = {
            "credit_card": "Credit Card",
            "paypal": "PayPal",
        }
        method_name = method_names.get(method, method)
        return {"message": f"Processed {amount} via {method_name}."}


class MonolithicRetailSystem:
    def __init__(self):
        self.cart = Cart()
        self.inventory = Inventory()
        self.payment = Payment()

    def add_inventory(self, item, quantity):
        return self.inventory.update_stock(item, quantity)

    def add_to_cart(self, item, quantity):
        stock_result = self.inventory.remove_stock(item, quantity)
        if "error" in stock_result:
            return stock_result
        return self.cart.add_item(item, quantity)

    def checkout(self, item, quantity, method, amount):
        cart_result = self.add_to_cart(item, quantity)
        if "error" in cart_result:
            return cart_result
        return self.payment.process_payment(amount, method)


if __name__ == "__main__":
    system = MonolithicRetailSystem()
    print(system.add_inventory("Laptop", 10))
    print(system.checkout("Laptop", 2, "credit_card", 2000))

