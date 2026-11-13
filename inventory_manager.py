import json
import os

from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


FILE_NAME = "inventory.json"


def save_inventory(inventory):
    data = []

    for product in inventory.get_all_products():
        product_data = {
            "product_id": product.product_id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock
        }

        if isinstance(product, PhysicalProduct):
            product_data["type"] = "physical"
            product_data["weight"] = product.weight

        elif isinstance(product, DigitalProduct):
            product_data["type"] = "digital"
            product_data["download_size"] = product.download_size

        data.append(product_data)

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully.")


def load_inventory():
    inventory = Inventory()

    if not os.path.exists(FILE_NAME):
        return inventory

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        for item in data:
            if item["type"] == "physical":
                product = PhysicalProduct(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["weight"]
                )

            elif item["type"] == "digital":
                product = DigitalProduct(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["download_size"]
                )

            else:
                continue

            inventory.add_product(product)

        print("Inventory loaded successfully.")

    except (json.JSONDecodeError, KeyError, ValueError, TypeError) as error:
        print(f"Error loading inventory: {error}")

    return inventory


def add_product_menu(inventory):
    print("\n1. Physical Product")
    print("2. Digital Product")

    choice = input("Select product type: ")

    if choice not in ("1", "2"):
        print("Invalid product type.")
        return

    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")

    try:
        price = float(input("Enter Price: "))
        stock = int(input("Enter Stock: "))

        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return

        if choice == "1":
            weight = float(input("Enter Weight (kg): "))

            if weight < 0:
                print("Weight cannot be negative.")
                return

            product = PhysicalProduct(
                product_id, name, price, stock, weight
            )

        else:
            download_size = float(
                input("Enter Download Size (MB): ")
            )

            if download_size < 0:
                print("Download size cannot be negative.")
                return

            product = DigitalProduct(
                product_id, name, price, stock, download_size
            )

        inventory.add_product(product)

    except ValueError:
        print("Invalid number entered.")


def update_stock_menu(inventory):
    product_id = input("Enter Product ID: ")

    try:
        quantity = int(
            input("Enter quantity to add/remove: ")
        )

        inventory.update_stock(product_id, quantity)

    except ValueError:
        print("Please enter a valid integer.")


def search_product_menu(inventory):
    product_id = input("Enter Product ID: ")

    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
    else:
        product.display_information()
        print(product.get_fulfilment_info())


def main():
    inventory = load_inventory()

    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            add_product_menu(inventory)

        elif choice == "3":
            update_stock_menu(inventory)

        elif choice == "4":
            search_product_menu(inventory)

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            save_inventory(inventory)
            print("Exiting Inventory Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
