import pytest

from src.product import Category, Product


def test_product_init(product_1, product_2):
    """Тест на инициализацию класса"""
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5

    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8


def test_category_init(category_1, category_2):
    """Тест на инициализацию класса"""
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Описание"
    assert len(category_1.products_in_list) == 2

    """ Тест на подсчет количества продуктов и категорий."""
    assert category_1.product_count == 5
    assert category_2.product_count == 5

    assert category_1.category_count == 2
    assert category_2.category_count == 2


def test_list_of_products_property(category_1):
    """Тест на работу геттера."""
    assert (
        category_1.products
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_add_product():
    """Тест на добавление экземпляра."""
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    assert product4.name == '55" QLED 4K'
    assert product4.description == "Фоновая подсветка"
    assert product4.price == 123000.0
    assert product4.quantity == 7


def test_add_product_error(bag1):
    """Тест на выбрасывание ошибки при добавлении экземпляра другого класса."""
    with pytest.raises(TypeError):
        Category.add_product(bag1)


def test_new_product_with_changing_price(capsys):
    """Тест на создание экземпляра из словаря и изменения атрибута цены."""
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5

    new_product.price = 200000.0
    assert new_product.price == 200000.0
    new_product.price = -100
    message = capsys.readouterr()
    assert (
        message.out.strip().split("\n")[-1]
        == "Цена не должна быть нулевая или отрицательная"
    )
    assert new_product.price == 200000.0
    new_product.price = 0
    assert new_product.price == 200000.0


Category.category_count = 0


def test_counter():
    """Тест на работоспособность счетчиков."""

    Category(
        "Смартфоны",
        "Описание",
        [
            Product(
                "Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5,
            ),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )
    Category(
        "Телевизоры",
        "Описание",
        [Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_product_str(product_1, product_2):
    """Тест на строковое представление продукта."""
    assert str(product_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product_2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_product_add(product_1, product_2):
    """Тест на корректную сумму произведений цены на количество у двух объектов."""
    assert product_1 + product_2 == 2580000.0


def test_category_str(category_1):
    """Тест на строковое представление категории."""
    assert str(category_1) == "Смартфоны, количество продуктов: 13 шт. "


def test_product_invalid():
    """Тест на выбрасывание исключения."""
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_middle_price(category_1):
    """Тест на корректность расчета среднего значения цены в списке продуктов категории."""
    assert category_1.middle_price() == 195000.0


def test_middle_price_empty():
    """Тест на обработку категории с пустым списком."""
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price() == 0
