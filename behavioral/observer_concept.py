from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Observer(ABC):
    """
    Интерфейс Наблюдателя объявляет метод уведомления, который издатели
    используют для оповещения своих подписчиков.
    """

    @abstractmethod
    def update(self, subject: 'Subject') -> None:
        """
        Получить обновление от субъекта.
        """
        pass


class ConcreteObserverA(Observer):
    def update(self, subject: 'Subject') -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: 'Subject') -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


class Subject(ABC):
    """
    Интерфейс издателя объявляет набор методов для управлениями подписчиками.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Присоединяет наблюдателя к издателю.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Отсоединяет наблюдателя от издателя.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Уведомляет всех наблюдателей о событии.
        """
        pass


class ConcreteSubject(Subject):
    """
    Издатель владеет некоторым важным состоянием и оповещает наблюдателей о его
    изменениях.
    """

    _state: int = None
    """
    Для удобства в этой переменной хранится состояние Издателя, необходимое всем
    подписчикам.
    """

    _observers: List[Observer] = []
    """
    Список подписчиков. В реальной жизни список подписчиков может храниться в
    более подробном виде (классифицируется по типу события и т.д.)
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Обычно логика подписки – только часть того, что делает Издатель.
        Издатели часто содержат некоторую важную бизнес-логику, которая
        запускает метод уведомления всякий раз, когда должно произойти что-то
        важное (или после этого).
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


if __name__ == "__main__":
    subj = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subj.attach(observer_a)

    observer_b = ConcreteObserverB()
    subj.attach(observer_b)

    subj.some_business_logic()
    subj.some_business_logic()

    subj.detach(observer_a)

    subj.some_business_logic()
