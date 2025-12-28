class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id  # unique id for lookup
        self.name = name
        self.price = price

    def display(self):
        """Display basic info of the product."""
        print(f"{self.product_id}. {self.name} - Rs. {self.price}")