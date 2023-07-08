# Import the Product class from the "product" module
from product import Product
# Import the datetime and timedelta classes from the "datetime" module
from datetime import datetime, timedelta


class ProductNode:
    def __init__(self, product: Product):
        self.product = product
        self.next = None

    def __str__(self):
        return str(self.product)


class Perishable:
    def __init__(self):
        self.head = None  # The head of the linked list
        self.tail = None  # The tail of the linked list

    def is_empty(self):
        return self.head is None

    def add_perishable_product(self, product: Product):
        name = product.name.lower()
        element = ProductNode(product)
        if self.is_empty():
            # If the list is empty, the new element becomes both the head and the tail of the list
            self.head = element
            self.tail = element
        else:
            buffer = self.head
            while buffer is not None:
                if buffer.product.name.lower() == name:
                    break  # The product already exists, exit the loop
                elif buffer.next is None:
                    # Reached the end of the list, add the new element at the end
                    element.next = None
                    buffer.next = element
                    self.tail = element
                    break
                buffer = buffer.next

    def add_perishable_product_at_start(self, product: Product):
        name = product.name.lower()
        element = ProductNode(product)
        if self.is_empty():
            # If the list is empty, the new element becomes both the head and the tail of the list
            self.head = element
            self.tail = element
        else:
            product_found = False
            buffer = self.head
            while buffer is not None:
                if buffer.product.name.lower() == name:
                    product_found = True  # The product already exists, signal it
                    break
                buffer = buffer.next
            if not product_found:
                element.next = buffer
                self.head = element

    def display_perishable_products(self):
        # Display the perishable products
        if self.is_empty():  # If the list is empty, signal it
            print("No elements")
        else:  # Traverse all elements and display them
            buffer = self.head
            while buffer is not None:
                print(buffer)
                buffer = buffer.next

    def search_perishable_product(self, name):
        # Search for a perishable product
        name = name.lower()
        product = None
        if not self.is_empty():
            buffer = self.head
            while buffer is not None:
                if buffer.product.get_name().lower() == name:
                    product = buffer.product
                    break
                buffer = buffer.next
        return product

    def display_product(self, name):
        product = self.search_perishable_product(name)
        if product:
            product.display_product()

    def remove_perishable_product(self, name):
        name = name.lower()

        if self.is_empty():
            raise IndexError("There are no products")
        else:
            buffer = self.head
            if buffer.product.name.lower() == name:
                # If the product to be removed is at the head of the list, update the head
                self.head = buffer.next
            else:
                while buffer is not None:
                    if buffer.product.name.lower() == name:
                        break  # Found the product to be removed
                    previous = buffer
                    buffer = buffer.next
                if buffer is None:
                    return
                previous.next = buffer.next

    def expire_product(self):
        current_date = datetime.now()
        future_date = current_date + timedelta(days=30)
        buffer = self.head
        while buffer is not None:
            expiration_date = datetime.strptime(
                buffer.product.expiration_date, "%Y-%m-%d")
            if expiration_date < future_date:
                print(buffer.product)
            buffer = buffer.next

    def update_perishable_product_quantity(self, name, quantity):
        name = name.lower()
        if self.is_empty():
            raise IndexError("There are no products")
        else:
            buffer = self.head
            while buffer is not None:
                if buffer.product.name.lower() == name:
                    buffer.product.set_quantity(quantity)
                    break
                buffer = buffer.next

    def display_perishable_quantity(self):
        if self.is_empty():
            buffer = self.head
            while buffer is not None:
                print(buffer.product.name + "  " +
                      str(buffer.product.quantity))
                buffer = buffer.next

    def display_perishable_unit_price(self):
        # Display the unit price of all products
        if not self.is_empty():
            buffer = self.head
            while buffer is not None:
                print(buffer.product.name + "  " +
                      str(buffer.product.price))
                buffer = buffer.next
