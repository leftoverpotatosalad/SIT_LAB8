
from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        supplier: Supplier
    ) -> None:
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.supplier: Supplier = supplier

    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    def update_stock(self, quantity: int) -> None:
        if self.__stock + quantity >= 0:
            self.__stock += quantity
            print("Stock updated successfully.")
        else:
            print("Insufficient stock.")

    def display_information(self) -> None:
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")
        print(f"Supplier: {self.supplier.name}")

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
