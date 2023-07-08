class ProductType:
    def __init__(self, product_type) -> None:
        self.product_type = product_type


"""This is a class that allows to register all the products in the supermarket.
The getters and setters respectively retrieve the information of each product
and modify them."""


class Product:
    def __init__(self, name: str, product_type: ProductType, price: float, quantity=0, expiration_date=None):
        self.name = name.lower()
        self.product_type = product_type
        self.price = price
        self.quantity = quantity
        self.expiration_date = expiration_date

    def __str__(self) -> str:
        return f"{self.name}, Type: {self.product_type}, Price: {self.price}, Quantity: {self.quantity}"

    # Get the product name
    def get_name(self):
        if self.name is not None:
            return self.name
        else:
            print("Error, product does not exist")

    # Set the product name
    def set_name(self, name):
        self.name = name

    def get_product_type(self):
        return self.product_type

    def set_product_type(self, product_type: ProductType):
        self.product_type = product_type

    # Get the product price
    def get_price(self):
        try:
            return self.price
        except:
            print("Error, price not defined")

    # Set the product price
    def set_price(self, price):
        assert type(price) == float and price > 0
        self.price = price

    # Get the product quantity
    def get_quantity(self):
        return self.quantity

    # Set the product quantity
    def set_quantity(self, quantity):
        assert quantity > 0 and int(
            quantity) == quantity, "The product quantity must be a positive integer"
        self.quantity = quantity

    # Get the product expiration date
    def get_expiration_date(self):
        if self.expiration_date:
            return self.expiration_date
        return "Non-perishable product"

    # Display the product information
    def display_product(self):
        print(f"Product:      {self.name}")
        print(f"Type:         {self.product_type}")
        print(f"Price:        {self.price}")
        print(f"Quantity:     {self.quantity}")
