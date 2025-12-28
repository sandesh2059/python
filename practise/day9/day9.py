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

