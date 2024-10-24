class PrintMixin:
    """Класс mixin для вывода на печать информации при инициализации."""

    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity}"
