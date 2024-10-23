from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    """Класс для представления продуктов."""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price  # приватный атрибут цены
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity
        super().__init__()

    def __str__(self):
        """Метод для возврата строки в формате 'Название продукта, X руб. Остаток: X шт.'."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод сложения, который возвращает сумму произведений цены на количество у двух объектов."""
        if type(other) is Product:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_info):
        """Класс-метод для получения экземпляра класса из словаря."""
        name = product_info.get("name")
        description = product_info.get("description")
        price = product_info.get("price")
        quantity = product_info.get("quantity")
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для обращения к приватному атрибуту цены."""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для изменения атрибута цены с проверкой на положительное значение."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = value


class Category:
    """Класс для представления продуктов."""

    name: str
    description: str
    __products: list[Product] = []

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Метод для инициализации класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products  # приватный атрибут списка товаров

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """Метод для вывода строки в формате 'Название категории, количество продуктов: X шт.'"""
        self.product_count = 0
        for product in self.__products:
            self.product_count += product.quantity
        return f"{self.name}, количество продуктов: {self.product_count} шт. "

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта базового класса и дочерних."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        """Геттер для вывода информации о продукте в формате строки."""
        products_str = ""

        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    def middle_price(self):
        """Метод расчета средней цены продукта в категории."""
        total = sum([product.price for product in self.__products])
        try:
            avg_price = total / len(self.__products)
        except ZeroDivisionError:  # обработка пустого списка продуктов в категории
            return 0
        else:
            return round(avg_price, 2)

    @property
    def products_in_list(self):
        """Геттер для вывода информации о продукте в формате списка."""
        return self.__products
