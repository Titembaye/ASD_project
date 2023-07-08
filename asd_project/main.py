from product import Product
from product_management import ProductManagement


def menu():
    print("Welcome! How can I assist you?\n")
    print("1. Add a product\n")
    print("2. Remove a product\n")
    print("3. Update the quantity of a product\n")
    print("4. Display all products\n")
    print("5. Display products expiring in 30 days\n")
    print("6. Search for a product\n")
    print("7. Display operations\n")


def display_menu():
    print("1. Display all products\n")
    print("2. Display perishable products\n")
    print("3. Display non-perishable products\n")


def create_product():
    repeat_price = True
    repeat_quantity = True
    name = input("Enter the name of the product:\n")
    type = input("Enter the type of the product:\n")

    while repeat_price:
        price = float(input("Enter the price of the product:\n"))
        assert price > 0, "The price cannot be zero or negative"
        repeat_price = False

    while repeat_quantity:
        quantity = int(input("Enter the quantity of the product:\n"))
        assert quantity > 0, "The quantity cannot be zero or negative"
        repeat_quantity = False

    print("Does the product have an expiration date? (Yes/No)\n")
    print("1. Yes, the product has an expiration date\n")
    print("2. No, the product does not have an expiration date\n")
    add_date = int(input())

    if add_date == 1:
        expiration_date = input(
            "Enter the expiration date (year-month-day):\n")
        product = Product(name, type, price, quantity, expiration_date)
    else:
        product = Product(name, type, price, quantity)

    return product


if __name__ == "__main__":
    product_management = ProductManagement()
    continue_program = "Yes"

    while continue_program.lower() == "yes":
        menu()
        choice = int(input("Please select an action:\n"))

        if choice == 1:
            product = create_product()
            product_management.add_product(product)

        elif choice == 2:
            product_to_remove = create_product()
            product_management.remove_product(product_to_remove)

        elif choice == 3:
            answer = input("Is the product perishable? (Yes/No): ")
            product_to_update = input("Please enter the name of the product: ")
            quantity = input("Enter the new quantity: ")
            if answer.lower() == "yes":
                product_management.perishable_product.update_quantity_perishable(
                    product_to_update, quantity)
            else:
                product_management.update_quantity(product_to_update, quantity)

        elif choice == 4:
            display_menu()
            display_choice = int(input())
            if display_choice == 1:
                product_management.display_all()
            elif display_choice == 2:
                product_management.perishable_product.display_perishable()
            elif display_choice == 3:
                product_management.non_perishable_product.display_non_perishable()

        elif choice == 5:
            product_management.perishable_product.expiring_products()

        elif choice == 6:
            product_name = input(
                "Enter the name of the product you're searching for: ")
            product_management.search_product(product_name)

        elif choice == 7:
            product_management.display_operations()

        else:
            print("Please select a number from 1 to 7")

        continue_program = input("Do you want to continue? (Yes/No): ")
