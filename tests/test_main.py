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
    assert (
        category_1.description
        == "Описание"
    )
    assert len(category_1.products) == 2

    """ Тест на подсчет количества продуктов и категорий"""
    assert category_1.product_count == 5
    assert category_2.product_count == 5

    assert category_1.category_count == 2
    assert category_2.category_count == 2
