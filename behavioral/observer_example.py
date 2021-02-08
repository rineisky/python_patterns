from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass


class Citizen(Observer):
    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str) -> None:
        print(f'{self.name} узнал следующее: {message}')


class Observable(ABC):
    def __init__(self) -> None:
        self.observers = []

    def register(self, observer: Observer) -> None:
        self.observers.append(observer)

    def notify_observers(self, message: str) -> None:
        for observer in self.observers:
            observer.update(message)


class Newspaper(Observable):
    def add_news(self, news: str) -> None:
        self.notify_observers(news)


if __name__ == '__main__':
    newspaper = Newspaper()
    newspaper.register(Citizen('Иван'))
    newspaper.register(Citizen('Василий'))
    newspaper.add_news('Наблюдатель - поведенческий шаблон проектирования')
