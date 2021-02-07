import inspect
from abc import ABCMeta, abstractmethod
from weakref import proxy


class Mediator(metaclass=ABCMeta):
    """
    Абстрактный канал общения между коллегами
    """

    @abstractmethod
    def send(self, message: str) -> None:
        """
        Отправка сообщения между коллегами
        """
        pass


class Colleague(metaclass=ABCMeta):
    """
    Абстрактный работник, который не против пообщаться со своими коллегами
    """

    def __init__(self, mediator: Mediator) -> None:
        """
        Constructor.

        :param mediator: канал общения с коллегами
        """
        self._mediator = proxy(mediator)

    @abstractmethod
    def send(self, message: str) -> None:
        """
        Отправка сообщения через канал общения
        """
        pass

    @abstractmethod
    def receive(self, message: str) -> None:
        """
        Получения сообщения через канал общения
        """
        pass


class SkypeBetweenTwoColleagues(Mediator):
    """
    Канал в скайпе для общения между двумя людьми
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        self._first = None
        self._second = None

    def set_first(self, first: Colleague) -> None:
        """
        Привязывает к каналу первого участника разговора
        """
        self._first = first

    def set_second(self, second: Colleague) -> None:
        """
        Привязывает к каналу второго участника разговора
        """
        self._second = second

    def send(self, message: str) -> None:
        sender = inspect.currentframe().f_back.f_locals['self']
        receiver = self._first if sender == self._second else self._second
        receiver.receive(message)


class Bill(Colleague):

    def send(self, message: str) -> None:
        self._mediator.send(message)

    def receive(self, message: str) -> None:
        print('Билл получил сообщение: {}'.format(message))


class Steve(Colleague):

    def send(self, message: str) -> None:
        self._mediator.send(message)

    def receive(self, message: str) -> None:
        print('Стив прочитал в скайпе сообщение: {}'.format(message))


if __name__ == '__main__':
    print('OUTPUT:')
    skype = SkypeBetweenTwoColleagues()
    bill = Bill(skype)
    steve = Steve(skype)
    skype.set_first(bill)
    skype.set_second(steve)
    bill.send('Начинай работать, бездельник!')
    steve.send('Нет')

'''
OUTPUT:
Стив прочитал в скайпе сообщение: Начинай работать, бездельник!
Билл получил сообщение: Нет
'''
