
from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


supplier = Supplier(
    "S001", "Creative Technology", "contact@example.com"
)

laptop = PhysicalProduct(
    "P001", "Laptop", 1200.0, 8, 2.5, supplier
)

game = DigitalProduct(
    "D001", "Minecraft", 39.90, 100, 1500.0, supplier
)

print("=== PHYSICAL PRODUCT ===")
show_product_details(laptop)

print("\n=== DIGITAL PRODUCT ===")
show_product_details(game)

print("\n=== INVENTORY TEST ===")
inventory = Inventory()
inventory.add_product(laptop)
inventory.add_product(game)

inventory.display_all()
