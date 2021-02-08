from abc import ABCMeta, abstractmethod


class Unit(metaclass=ABCMeta):
    """отряд может состоять из одного солдата или более, а также другого отряда"""

    @abstractmethod
    def info(self, tabs=0, prefix='', postfix='\n') -> None:
        pass


class Archer(Unit):
    """Лучник"""

    def info(self, tabs=0, prefix='', postfix='\n') -> None:
        print('\t' * tabs + prefix + f'лучник {id(self)}', end=postfix)


class Knight(Unit):
    """Рыцарь"""

    def info(self, tabs=0, prefix='', postfix='\n') -> None:
        print('\t' * tabs + prefix + f'рыцарь {id(self)}', end=postfix)


class Squad(Unit):
    """
    Компоновщик - отряд, состоящий более чем из одного человека. Также
    может включать в себя другие отряды-компоновщики.
    """

    def __init__(self):
        self._units = []

    def info(self, tabs=0, prefix='', postfix='\n') -> None:
        print('\t' * tabs + prefix + f"Отряд {id(self)}", end=postfix)
        for unit in self._units:
            unit.info(tabs + 1, '* ')

    def add(self, unit: Unit) -> None:
        self._units.append(unit)
        unit.info(0, '+ ', f' присоединился к отряду {id(self)}\n')

    def remove(self, unit: Unit) -> None:
        for unit in self._units:
            if unit == unit:
                self._units.remove(unit)
                unit.info(0, '- ', f' покинул отряд {id(self)}\n')
                break
        else:
            unit.info()
            print('в отряде {} не найден'.format(self.__hash__()))
            print()


if __name__ == '__main__':
    print('ЛОГ СЕРВЕРА:')
    squad = Squad()
    squad.add(Knight())
    knight = Knight()
    squad.add(knight)
    squad.add(Archer())
    squad.remove(knight)
    squad.info()
    squad_big = Squad()
    squad_big.add(squad)
    squad_big.info()
    squad_big.remove(squad)
