from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    """
    Контекст определяет интерфейс, представляющий интерес для клиентов. Он также
    хранит ссылку на экземпляр подкласса Состояния, который отображает текущее
    состояние Контекста.
    """
    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        Контекст позволяет изменять объект Состояния во время выполнения.
        """
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request_1(self):
        """
        Контекст делегирует часть своего поведения текущему объекту Состояния.
        """
        self._state.handle1()

    def request_2(self):
        self._state.handle2()


class State(ABC):
    """
    Базовый класс Состояния объявляет методы, которые должны реализовать все
    Конкретные Состояния, а также предоставляет обратную ссылку на объект
    Контекст, связанный с Состоянием. Эта обратная ссылка может использоваться
    Состояниями для передачи Контекста другому Состоянию.
    """
    _context: Context

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle_1(self) -> None:
        pass

    @abstractmethod
    def handle_2(self) -> None:
        pass


"""
Конкретные Состояния реализуют различные модели поведения, связанные с
состоянием Контекста.
"""


class ConcreteStateA(State):
    def handle_1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle_2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle_1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle_2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())


if __name__ == "__main__":
    ctx = Context(ConcreteStateA())
    ctx.request_1()
    ctx.request_2()
