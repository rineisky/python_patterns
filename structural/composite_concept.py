from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    Базовый класс Компонент объявляет общие операции как для простых, так и для
    сложных объектов структуры.
    """
    _parent: 'Component'

    @property
    def parent(self) -> 'Component':
        return self._parent

    @parent.setter
    def parent(self, parent: 'Component'):
        """
        При необходимости базовый Компонент может объявить интерфейс для
        установки и получения родителя компонента в древовидной структуре. Он
        также может предоставить некоторую реализацию по умолчанию для этих
        методов.
        """
        self._parent = parent

    def add(self, component: 'Component') -> None:
        pass

    def remove(self, component: 'Component') -> None:
        pass

    @abstractmethod
    def operation(self) -> str:
        """
        Базовый Компонент может сам реализовать некоторое поведение по умолчанию
        или поручить это конкретным классам, объявив метод, содержащий поведение
        абстрактным.
        """
        pass

    def is_composite(self) -> bool:
        """
        Вы можете предоставить метод, который позволит клиентскому коду понять,
        может ли компонент иметь вложенные объекты.
        """
        return False


class Leaf(Component):
    """
    Класс Лист представляет собой конечные объекты структуры. Лист не может
    иметь вложенных компонентов.

    Обычно объекты Листьев выполняют фактическую работу, тогда как объекты
    Контейнера лишь делегируют работу своим подкомпонентам.
    """

    def operation(self) -> str:
        return "Лист"


class Composite(Component):
    """
    Класс Контейнер содержит сложные компоненты, которые могут иметь вложенные
    компоненты. Обычно объекты Контейнеры делегируют фактическую работу своим
    детям, а затем «суммируют» результат.
    """
    _children: List[Component]

    def __init__(self) -> None:
        self._children = []

    """
    Объект контейнера может как добавлять компоненты в свой список вложенных
    компонентов, так и удалять их, как простые, так и сложные.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        Контейнер выполняет свою основную логику особым образом. Он проходит
        рекурсивно через всех своих детей, собирая и суммируя их результаты.
        Поскольку потомки контейнера передают эти вызовы своим потомкам и так
        далее, в результате обходится всё дерево объектов.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Ветка({'+'.join(results)})"


def client_code(component: Component) -> None:
    """
    Клиентский код работает со всеми компонентами через базовый интерфейс.
    """
    print(f"RESULT: {component.operation()}")


def client_code2(component1: Component, component2: Component) -> None:
    """
    Благодаря тому, что операции управления потомками объявлены в базовом классе
    Компонента, клиентский код может работать как с простыми, так и со сложными
    компонентами, вне зависимости от их конкретных классов.
    """
    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}")


if __name__ == "__main__":
    simple = Leaf()
    print("Client: я могу получить простой компонент:")
    client_code(simple)
    print("\n")

    tree = Composite()
    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())
    branch2 = Composite()
    branch2.add(Leaf())
    tree.add(branch1)
    tree.add(branch2)
    print("Client: я могу получить сложный компонент:")
    client_code(tree)
    print("\n")

    print("Client: мне не надо проверять типы классов компонентов, "
          "когда я работаю с деревом:")
    client_code2(tree, simple)
