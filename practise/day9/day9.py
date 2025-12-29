class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id  # unique id for lookup
        self.name = name
        self.price = price

    def display(self):
        """Display basic info of the product."""
        print(f"{self.product_id}. {self.name} - Rs. {self.price}")


class Cart:
    def __init__(self):
        # Each entry: {"product": Product obj, "quantity": int}
        self.items = []
    
    def add_product(self, product, quantity=1):

        """Add a product to the cart. If already exists, increase quantity."""
        # Check if product already in cart
        for item in self.items:
            if item["product"].product_id == product.product_id:
                item["quantity"] += quantity
                print(f"Added {quantity} more of {product.name} to cart.")
                return
        # If not found, append new entry
        self.items.append({"product": product, "quantity": quantity})
        print(f"Added {product.name} to cart.")

    
    def remove_product(self, product_id, quantity=1):
        """Remove quantity of a product or remove entirely if 0 left."""
        for item in self.items:
            if item["product"].product_id == product_id:
                if quantity >= item["quantity"]:
                    # Remove entire item
                    self.items.remove(item)
                    print(f"Removed {item['product'].name} from cart.")
                else:
                    item["quantity"] -= quantity
                    print(f"Removed {quantity} of {item['product'].name} from cart.")
                return
        print("Product not found in cart.")
    def calculate_total(self):
        """Return total price without discount."""
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total
    def display_cart(self):
        if not self.items:
            print("\nCart is empty.")
            return

        print("\n--- Your Cart ---")
        for item in self.items:
            p = item["product"]
            qty = item["quantity"]
            print(f"{p.name} x {qty} = Rs. {p.price * qty}")
        total = self.calculate_total()
        print(f"Total: Rs. {total}")

    def clear_cart(self):
        self.items = []

class Shop:
    def __init__(self):
        self.products = []
        self.cart = Cart()
def add_product_to_catalog(self, product):
        self.products.append(product)



