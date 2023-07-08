import numpy as np
from product import Product


class NonPerishable:
    def __init__(self):
        self.non_perishable_products = np.asarray([], dtype=object)

    def is_empty(self):
        # Check if the list of non-perishable products is empty
        if len(self.non_perishable_products) == 0:
            return True
        return False

    def add_non_perishable_product(self, product: Product):
        # Add a non-perishable product
        name = product.name.lower()
        if len(self.non_perishable_products) == 0:
            self.non_perishable_products = np.insert(
                self.non_perishable_products, 0, product)
        else:
            product_found = False
            for i in range(len(self.non_perishable_products)):
                if self.non_perishable_products[i].name.lower() == name:
                    product_found = True
                    break
            if not product_found:
                self.non_perishable_products = np.insert(
                    self.non_perishable_products, 0, product)

    def display_non_perishable(self):
        # Display all non-perishable products
        for product in self.non_perishable_products:
            print(product)

    def search_non_perishable_product(self, name):
        # Search for a non-perishable product by its name
        name = name.lower()
        index = None
        for i in range(len(self.non_perishable_products)):
            if self.non_perishable_products[i].name.lower() == name:
                index = i
        if index is not None:
            return self.non_perishable_products[index]
        else:
            return None

    def display_product(self, name):
        product = self.search_non_perishable_product(name)
        if product:
            product.display_product()

    def remove_non_perishable(self, name):
        # Remove a non-perishable product by its name
        name = name.lower()
        if len(self.non_perishable_products) == 0:
            raise IndexError("There are no non-perishable products")
        else:
            product_found = False
            for i in range(len(self.non_perishable_products)):
                if self.non_perishable_products[i].name.lower() == name:
                    product_found = True
                    break
            if product_found:
                self.non_perishable_products = np.delete(
                    self.non_perishable_products, i)
            else:
                print("The product does not exist")

    def update_non_perishable_quantity(self, name, quantity):
        # Update the quantity of a non-perishable product
        name = name.lower()
        if len(self.non_perishable_products) == 0:
            raise IndexError("There are no products")
        else:
            for i in range(len(self.non_perishable_products)):
                if self.non_perishable_products[i].name.lower() == name:
                    self.non_perishable_products[i].set_quantity(quantity)

    def display_non_perishable_quantity(self):
        # Display the quantity of all non-perishable products
        if not self.is_empty():
            for i in range(len(self.non_perishable_products)):
                print(self.non_perishable_products[i].name, "  " +
                      str(self.non_perishable_products[i].quantity))

    def display_non_perishable_unit_price(self):
        # Display the unit price of all non-perishable products
        if not self.is_empty():
            for i in range(len(self.non_perishable_products)):
                print(self.non_perishable_products[i].name, "  " +
                      str(self.non_perishable_products[i].price))
