import pytest

from src.main import Category, Product


@pytest.fixture
def product_1():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def product_2():
    return Product(
        name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8
    )


@pytest.fixture
def category_1():
    category_1 = Category(
        name="Смартфоны",
        description="Описание",
        products=[
            Product(
                name="Samsung Galaxy S23 Ultra",
                description="256GB, Серый цвет, 200MP камера",
                price=180000.0,
                quantity=5,
            ),
            Product(
                name="Iphone 15",
                description="512GB, Gray space",
                price=210000.0,
                quantity=8,
            ),
        ],
    )
    yield category_1
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def category_2():
    category_2 = Category(
        name="Телевизоры",
        description="Описание продукта",
        products=[
            Product(
                name="Имя первого",
                description="Описание первого",
                price=60000.0,
                quantity=5,
            ),
            Product(
                name="Имя второго",
                description="Описание второго",
                price=210000.0,
                quantity=8,
            ),
            Product(
                name="Имя третьего",
                description="Описание третьего",
                price=310000.0,
                quantity=2,
            ),
        ],
    )
    yield category_2
    Category.category_count = 0
    Category.product_count = 0
