
from product import Product


class Inventory:

    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            print("Error: Only products can be added.")
            return

        if self.search_product(product.product_id) is not None:
            print("Error: Product ID already exists.")
            return

        self.__products.append(product)
        print("Product added successfully.")

    def search_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.product_id == product_id:
                return product

        return None

    def find_product(self, product_id: str) -> Product | None:
        return self.search_product(product_id)

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)

        if product is not None:
            self.__products.remove(product)
            print("Product removed successfully.")
        else:
            print("Product not found.")

    def display_all(self) -> None:
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

    def update_stock(
        self,
        product_id: str,
        quantity: int
    ) -> None:
        product = self.search_product(product_id)

        if product is None:
            print("Product not found.")
            return

        product.update_stock(quantity)

    def get_all_products(self) -> list[Product]:
        return self.__products.copy()
