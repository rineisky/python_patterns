from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """
    Абстрактный наблюдатель
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        Получение нового сообщения
        """
        pass


class Observable(metaclass=ABCMeta):
    """
    Абстрактный наблюдаемый
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        self.observers = []  # инициализация списка наблюдателей

    def register(self, observer: Observer) -> None:
        """
        Регистрация нового наблюдателя на подписку
        """
        self.observers.append(observer)

    def notify_observers(self, message: str) -> None:
        """
        Передача сообщения всем наблюдателям, подписанным на события
        данного объекта наблюдаемого класса
        """
        for observer in self.observers:
            observer.update(message)


class Newspaper(Observable):
    """
    Газета, за новостями в которой следят тысячи людей
    """

    def add_news(self, news: str) -> None:
        """
        Выпуск очередной новости
        """
        self.notify_observers(news)


class Citizen(Observer):
    """
    Обычный гражданин, который любит читнуть с утра любимую газетку
    """

    def __init__(self, name: str) -> None:
        """
        Constructor.

        :param name: имя гражданина, чтоб не спутать его с кем-то другим
        """
        self.name = name

    def update(self, message: str) -> None:
        """
        Получение очередной новости
        """
        print(f'{self.name} узнал следующее: {message}')


if __name__ == '__main__':
    newspaper = Newspaper()  # создаем небольшую газету
    newspaper.register(Citizen('Иван'))  # добавляем двух человек, которые
    newspaper.register(Citizen('Василий'))  # ... ее регулярно выписывают
    # ... и вбрасываем очередную газетную утку
    newspaper.add_news('Наблюдатель - поведенческий шаблон проектирования')

'''
Иван узнал следующее: Наблюдатель - поведенческий шаблон проектирования
Василий узнал следующее: Наблюдатель - поведенческий шаблон проектирования
'''
