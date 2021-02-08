from abc import ABC, abstractmethod


class Product(ABC):
    """
    Абстрактный класс (интерфейс) для продуктов объявляет методы, которые должны
    реализовать конкретные продукты
    """

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "<Result of the ConcreteProduct1>"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "<Result of the ConcreteProduct2>}"


class Creator(ABC):
    """
    Класс Создатель объявляет фабричный метод, который должен возвращать объект
    класса Продукт. Подклассы Создателя обычно предоставляют реализацию этого
    метода.
    """

    @abstractmethod
    def factory_method(self):
        """
        Обратите внимание, что Создатель может также обеспечить реализацию
        фабричного метода по умолчанию.
        """
        pass

    def some_operation(self) -> str:
        """
        Также заметьте, что, несмотря на название, основная обязанность
        Создателя не заключается в создании продуктов. Обычно он содержит
        некоторую базовую бизнес-логику, которая основана на объектах Продуктов,
        возвращаемых фабричным методом. Подклассы могут косвенно изменять эту
        бизнес-логику, переопределяя фабричный метод и возвращая из него другой
        тип продукта.
        """

        # Вызываем фабричный метод, чтобы получить объект-продукт.
        product = self.factory_method()

        # Далее, работаем с этим продуктом.
        result = f"Creator: результат операции {product.operation()}"

        return result


"""
Конкретные Создатели переопределяют фабричный метод для того, чтобы изменить тип
результирующего продукта.
"""


class ConcreteCreator1(Creator):
    """
    Обратите внимание, что сигнатура метода по-прежнему использует тип
    абстрактного продукта, хотя фактически из метода возвращается конкретный
    продукт. Таким образом, Создатель может оставаться независимым от конкретных
    классов продуктов.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


def client_code(creator: Creator) -> None:
    """
    Клиентский код работает с экземпляром конкретного создателя, хотя и через
    его базовый интерфейс. Пока клиент продолжает работать с создателем через
    базовый интерфейс, вы можете передать ему любой подкласс создателя.
    """
    print(f"{creator.some_operation()}")


if __name__ == "__main__":
    print("App: запуск с ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")
    print("App: запуск с ConcreteCreator2.")
    client_code(ConcreteCreator2())
