from abc import ABCMeta, abstractmethod
from typing import List


class Spy(metaclass=ABCMeta):
    """
    Шпион - посетитель
    """

    @abstractmethod
    def visit_military_base(self, military_base: 'MilitaryBase') -> None:
        """
        Посетить военную базу морского флота
        """
        pass

    @abstractmethod
    def visit_headquarters(self, headquarters: 'Headquarters') -> None:
        """
        Посетить центральный штаб армии
        """
        pass


class MilitaryFacility(metaclass=ABCMeta):
    """
    Военный объект - посещаемый объект
    """

    @abstractmethod
    def accept(self, spy: Spy) -> None:
        """
        Принять шпиона-посетителя
        """
        pass


class MilitaryBase(MilitaryFacility):
    """
    Военная база подводного флота
    """

    def __init__(self) -> None:
        self._secret_draftings = 1
        self._nuclear_submarines = 1

    def __repr__(self) -> str:
        return 'На военной базе находится {} атомных подводных лодок и {} секретных чертежей'.format(
            self._nuclear_submarines, self._secret_draftings
        )

    def accept(self, spy: Spy) -> None:
        spy.visit_military_base(self)

    def remove_secret_draftings(self) -> None:
        if self._secret_draftings:
            self._secret_draftings -= 1

    def remove_nuclear_submarine(self) -> None:
        if self._nuclear_submarines:
            self._nuclear_submarines -= 1

    @property
    def is_combat_ready(self) -> bool:
        return self._nuclear_submarines > 0


class Headquarters(MilitaryFacility):
    """
    Центральный штаб армии
    """

    def __init__(self) -> None:
        self._generals = 3
        self._secret_documents = 2

    def __repr__(self) -> str:
        return 'В штабе находится {} генералов и {} секретных документов'.format(
            self._generals, self._secret_documents
        )

    def accept(self, spy: Spy) -> None:
        spy.visit_headquarters(self)

    def remove_general(self) -> None:
        if self._generals:
            self._generals -= 1

    def remove_secret_documents(self) -> None:
        if self._secret_documents:
            self._secret_documents -= 1

    @property
    def is_command_ready(self) -> bool:
        return self._generals > 0


class ScoutSpy(Spy):
    """
    Разведчик (конкретный шпион)
    """

    def __init__(self):
        self._collected_info = {}

    # Здесь мы уже знаем конкретный тип объекта
    def visit_military_base(self, military_base: MilitaryBase) -> None:
        self._collected_info['base'] = 'Военная база:\n\t{}\n\tБоеготовность: {}'.format(
            str(military_base),
            'Да' if military_base.is_combat_ready else 'Нет'
        )

    def visit_headquarters(self, headquarters: Headquarters) -> None:
        self._collected_info['headquarters'] = 'Центральный штаб:\n\t{}\n\tКомандование: {}'.format(
            str(headquarters),
            'Функционирует' if headquarters.is_command_ready else 'Не функционирует'
        )

    def report(self) -> str:
        return 'Информация от разведчика:\n{}\n'.format(
            '\n'.join(self._collected_info.values())
        )


class JamesBond(Spy):
    """
    Джеймс Бонд (другой конкретный шпион)
    """

    def visit_military_base(self, military_base: MilitaryBase) -> None:
        # Джеймс Бонд посещает военную базу
        military_base.remove_secret_draftings()  # похищает секретные чертежи
        military_base.remove_nuclear_submarine()  # и напоследок взрывает атомную подводную лодку

    def visit_headquarters(self, headquarters: Headquarters) -> None:
        # Джеймс Бонд посещает штаб
        headquarters.remove_general()  # ...
        headquarters.remove_general()  # ...
        headquarters.remove_secret_documents()  # ...
        headquarters.remove_general()  # последовтельно уничтожает всех генералов
        headquarters.remove_secret_documents()  # и похищает все секретные документы


if __name__ == '__main__':
    base = MilitaryBase()
    hq = Headquarters()

    # Не важно какой именно MilitaryFacility
    facilities = [base, hq]  # type: List[MilitaryFacility]

    scout = ScoutSpy()
    print('Отправляем разведчика...\n')
    for f in facilities:
        f.accept(scout)

    print(scout.report())

    print('Отправляем Бонда на задание...\n')

    spy = JamesBond()
    for f in facilities:
        f.accept(spy)

    print('Отправляем разведчика обновить данные...\n')
    for f in facilities:
        f.accept(scout)

    print(scout.report())

"""
OUTPUT:

Отправляем разведчика...

Информация от разведчика:
Центральный штаб:
    В штабе находится 3 генералов и 2 секретных документов
    Командование: Функционирует
Военная база:
    На военной базе находится 1 атомных подводных лодок и 1 секретных чертежей
    Боеготовность: Да

Отправляем Бонда на задание...

Отправляем разведчика обновить данные...

Информация от разведчика:
Центральный штаб:
    В штабе находится 0 генералов и 0 секретных документов
    Командование: Не функционирует
Военная база:
    На военной базе находится 0 атомных подводных лодок и 0 секретных чертежей
    Боеготовность: Нет

"""
