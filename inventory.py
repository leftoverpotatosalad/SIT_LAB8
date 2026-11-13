
from product import Product


class Inventory:

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            print("Error: Only products can be added.")
            return

        if self.search_product(product.product_id) is not None:
            print("Error: Product ID already exists.")
            return

        self.__products.append(product)
        print("Product added successfully.")

    def search_product(self, product_id):
        for product in self.__products:
            if product.product_id == product_id:
                return product

        return None

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            print("------------------------------")
            product.display_information()
            print(product.get_fulfilment_info())

            if hasattr(product, "calculate_shipping_cost"):
                print(
                    f"Shipping Cost: "
                    f"${product.calculate_shipping_cost():.2f}"
                )

        print("------------------------------")

    def update_stock(self, product_id, quantity):
        product = self.search_product(product_id)

        if product is None:
            print("Product not found.")
            return

        product.update_stock(quantity)

    def get_all_products(self):
        return self.__products.copy()
