from abc import abstractmethod, ABC


class Government(ABC):
    """Форма правления"""
    name: str

    @abstractmethod
    def set_name(self):
        pass

    def __init__(self):
        self.set_name()

    def __str__(self):
        return f"Форма правления: {self.name}"


class Monarchy(Government):
    def set_name(self):
        self.name = 'монархия'


class Republic(Government):
    def set_name(self):
        self.name = 'республика'


class GovernmentCreator(ABC):
    """Интерфейс создателей форм правления"""
    government: Government

    def __str__(self):
        return str(self.government)

    @abstractmethod
    def set_government(self):
        pass


class MonarchyGovernment(GovernmentCreator):
    def set_government(self):
        self.government = Monarchy()


class RepublicGovernment(GovernmentCreator):
    def set_government(self):
        self.government = Republic()


if __name__ == '__main__':
    monarchy = MonarchyGovernment()
    monarchy.set_government()
    print(monarchy)
    republic = RepublicGovernment()
    republic.set_government()
    print(republic)
