from product import Product
from datetime import datetime, timedelta
from perishable import Perishable
from non_perishable import NonPerishable


class Operation:
    def __init__(self, operation, date=datetime.now()):
        self.operation = operation
        self.date = date
        self.next = None

    def __str__(self):
        return f"{self.operation}    {self.date}"


class OperationStack:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def __str__(self):
        if not self.is_empty():
            return self.head.__str__()

    def add_operation(self, operation):
        operation = Operation(operation)
        if self.is_empty():
            self.head = operation
            self.tail = operation
        else:
            operation.next = self.head
            self.head = operation

    def recent_operations(self):
        current_date = datetime.now()
        date = current_date - timedelta(days=7)
        buffer = self.head
        while buffer is not None:
            if buffer.date > date:
                print(buffer.operation)
            buffer = buffer.next

    def display_operations(self):
        operation = "Display all products"
        operation = Operation(operation)
        if self.head is None:
            print("No elements")
        else:
            buffer = self.head
            while buffer is not None:
                print(buffer)
                buffer = buffer.next


class ProductManagement:
    def __init__(self):
        self.perishable_product = Perishable()
        self.non_perishable_product = NonPerishable()
        self.operation_stack = OperationStack()

    def add_product(self, product):
        name = product.name.lower()
        operation = f"Add {name}"
        operation = Operation(operation)
        if product.expiration_date is None:
            self.non_perishable_product.add_non_perishable_product(product)
        elif product.expiration_date:
            self.perishable_product.add_perishable_product(product)
        self.operation_stack.add_operation(operation)

    def display_all(self):
        operation = "Display all products"
        operation = Operation(operation)
        if not self.perishable_product.is_empty():
            self.perishable_product.display_perishable()
        if not self.non_perishable_product.is_empty():
            self.non_perishable_product.display_non_perishable()
        self.operation_stack.add_operation(operation)

    def display_operations(self):
        if not self.operation_stack.is_empty():
            self.operation_stack.display_operations()
        else:
            print("There are no operations to display")

    def search_product(self, name):
        name = name.lower()
        operation = f"Search for {name}"
        operation = Operation(operation)
        product = self.perishable_product.search_perishable_product(name)
        if product is None:
            product = self.non_perishable_product.search_non_perishable_product(
                name)
            if product is None:
                return None
        if product.name == name:
            return product
        self.operation_stack.add_operation(operation)

    def display_product(self, name):
        product = self.search_product(name)
        if product:
            product.display_product()
            if product.expiration_date:
                print(f"Expiration date: {product.expiration_date}")

    def remove_product(self, name):
        name = name.lower()
        operation = f"Remove {name}"
        operation = Operation(operation)
        product = self.search_product(name)
        if product is not None:
            if product.expiration_date:
                self.perishable_product.remove_perishable_product(name)
            else:
                self.non_perishable_product.remove_non_perishable_product(name)
        self.operation_stack.add_operation(operation)

    def update_quantity(self, name, quantity):
        name = name.lower()
        operation = f"Update quantity of {name}"
        operation = Operation(operation)
        product = self.search_product(name)
        if product is not None:
            if product.expiration_date:
                self.perishable_product.update_quantity_perishable(
                    name, quantity)
            else:
                self.non_perishable_product.update_quantity_non_perishable(
                    name, quantity)
        self.operation_stack.add_operation(operation)

    def display_quantity(self):
        if self.perishable_product:
            self.perishable_product.display_quantity_perishable()
        if self.non_perishable_product:
            self.non_perishable_product.display_quantity_non_perishable()

    def display_unit_price(self):
        if self.perishable_product:
            self.perishable_product.display_unit_price_perishable()
        if self.non_perishable_product:
            self.non_perishable_product.display_unit_price_non_perishable()
