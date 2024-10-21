class Product:
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
        self.quantity = quantity

    def __str__(self):
        """Метод для возврата строки в формате 'Название продукта, X руб. Остаток: X шт.'."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод сложения, который возвращает сумму произведений цены на количество у двух объектов."""
        return self.price * self.quantity + other.price * other.quantity

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
        """Метод для добавления продукта."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для вывода информации о продукте в формате строки."""
        products_str = ""

        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products_in_list(self):
        """Геттер для вывода информации о продукте в формате списка."""
        return self.__products


# if __name__ == "__main__":
#     product1 = Product(
#         "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
#     )
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     print(product1.name)
#     print(product1.description)
#     print(product1.price)
#     print(product1.quantity)
#
#     print(product2.name)
#     print(product2.description)
#     print(product2.price)
#     print(product2.quantity)
#
#     print(product3.name)
#     print(product3.description)
#     print(product3.price)
#     print(product3.quantity)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3],
#     )
#
#     print(category1.name == "Смартфоны")
#     print(category1.description)
#     print(len(category1.products))
#     print(category1.category_count)
#     print(category1.product_count)
#
#     product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
#     category2 = Category(
#         "Телевизоры",
#         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
#         [product4],
#     )
#
#     print(category2.name)
#     print(category2.description)
#     print(len(category2.products))
#     print(category2.products)
#
#     print(Category.category_count)
#     print(Category.product_count)


# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
#     print(category1.products)
#     product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
#     category1.add_product(product4)
#     print(category1.products)
#     print(category1.product_count)
#
#     new_product = Product.new_product(
#         {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
#          "quantity": 5})
#     print(new_product.name)
#     print(new_product.description)
#     print(new_product.price)
#     print(new_product.quantity)
#
#     new_product.price = 800
#     print(new_product.price)
#
#     new_product.price = -100
#     print(new_product.price)
#     new_product.price = 0
#     print(new_product.price)

# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     print(str(product1))
#     print(str(product2))
#     print(str(product3))
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
#     print(str(category1))
#
#     print(category1.products)
#
#     print(product1 + product2)
#     print(product1 + product3)
#     print(product2 + product3)
