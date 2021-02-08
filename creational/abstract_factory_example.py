from abc import ABC, abstractmethod


class AbstractTable(ABC):
    @abstractmethod
    def about_table(self):
        pass


class WoodenTable(AbstractTable):
    def about_table(self):
        return 'деревянный стол'


class PlasticTable(AbstractTable):
    def about_table(self):
        return 'пластиковый стол'


class AbstractChair(ABC):
    @abstractmethod
    def about_chair(self):
        pass


class WoodenChair(AbstractChair):
    def about_chair(self):
        return 'деревянный стул'


class PlasticChair(AbstractChair):
    def about_chair(self):
        return 'пластиковый стул'


class FurnitureFactory(ABC):
    @abstractmethod
    def create_table(self) -> AbstractTable:
        pass

    @abstractmethod
    def create_chair(self) -> AbstractChair:
        pass


class WoodenFactory(FurnitureFactory):
    def create_table(self) -> AbstractTable:
        return WoodenTable()

    def create_chair(self) -> AbstractChair:
        return WoodenChair()


class PlasticFactory(FurnitureFactory):
    def create_table(self) -> AbstractTable:
        return PlasticTable()

    def create_chair(self) -> AbstractChair:
        return PlasticChair()


def about_my_furniture(table, chair):
    print(f'У нас {table.about_table()} и {chair.about_chair()}')


if __name__ == '__main__':
    wooden_factory = WoodenFactory()
    plastic_factory = PlasticFactory()

    print('Покупаем деревянную мебель в квартиру:')
    wooden_table = wooden_factory.create_table()
    wooden_chair = wooden_factory.create_chair()
    about_my_furniture(wooden_table, wooden_chair)

    print('Покупаем пластиковую мебель для улицы')
    plastic_table = plastic_factory.create_table()
    plastic_chair = plastic_factory.create_chair()
    about_my_furniture(plastic_table, plastic_chair)
