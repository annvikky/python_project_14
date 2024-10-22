from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс с абстрактным методом инициализации."""

    @abstractmethod
    def __init__(self):
        pass
