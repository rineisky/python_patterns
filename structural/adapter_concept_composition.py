class Target:
    """
    Целевой класс объявляет интерфейс, с которым может работать клиентский код.
    """

    def request(self) -> str:
        return "Target: стандартное поведение"


class Adaptee:
    """
    Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
    несовместим с существующим клиентским кодом. Адаптируемый класс нуждается в
    некоторой доработке, прежде чем клиентский код сможет его использовать.
    """

    def specific_request(self) -> str:
        return "еинедевоп еончифицепс"


class Adapter(Target):
    """
    Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом благодаря агрегации.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    """
    Клиентский код поддерживает все классы, использующие интерфейс Target.
    """
    print(target.request())


if __name__ == "__main__":
    print("Client: я могу работать с Target объектами")
    tg = Target()
    client_code(tg)
    print("\n")

    adt = Adaptee()
    print("Client: у класса Adaptee не подходящий интерфейс")
    print(f"Adaptee: {adt.specific_request()}")
    print("\n")

    print("Client: но я могу работать с ним через Adapter")
    adapter = Adapter(adt)
    client_code(adapter)
