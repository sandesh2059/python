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

def show_products(self):
    if not self.products:
        print("No products in catalog.")
        return
    print("\n--- Available Products ---")
    for p in self.products:
        p.display()
def find_product(self, product_id):
        """Return Product object matching the id, or None."""
        for p in self.products:
            if p.product_id == product_id:
                return p
        return None
def checkout(self):
        if not self.cart.items:
            print("Cart is empty. Nothing to checkout.")
            return

        total = self.cart.calculate_total()
        discount = 0
        if total > 50000:
            discount = total * 0.10  # 10% discount
            total_after_discount = total - discount
            print(f"\nCongratulations! You got a 10% discount of Rs. {discount:.2f}")
            print(f"Total after discount: Rs. {total_after_discount:.2f}")
        else:
            total_after_discount = total
            print("\nNo discount applied.")
            print(f"Total to pay: Rs. {total_after_discount}")

        # After checkout, clear cart
        self.cart.clear_cart()
        print("Checkout complete. Thank you for shopping!\n")

def main_menu():
    shop = Shop()
    shop.add_product_to_catalog(Product(1, "Laptop", 80000))
    shop.add_product_to_catalog(Product(2, "Smartphone", 40000))
    shop.add_product_to_catalog(Product(3, "Headphones", 3000))
    shop.add_product_to_catalog(Product(4, "Keyboard", 2000))
    shop.add_product_to_catalog(Product(5, "Mouse", 1500))
    while True:
        print("\n===== SHOP MENU =====")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Remove Product from Cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            shop.show_products()
        
        elif choice == '2':
            shop.show_products()
            try:
                pid = int(input("Enter Product ID to add: "))
                qty = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue








