import pytest


def test_grass_init(grass1):
    """Тест на инициализацию дочернего класса."""
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_grass_add(grass1, grass2):
    """Тест на корректность сложения продуктов внутри класса"""
    assert grass1 + grass2 == 16750.0


def test_grass_add_error(grass1):
    """Тест на выбрасывание ошибки при сложении продуктов вне класса"""
    with pytest.raises(TypeError):
        grass1 + 1
