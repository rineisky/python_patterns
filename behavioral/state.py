from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    @abstractmethod
    def eat(self) -> str:
        pass

    @abstractmethod
    def find_food(self) -> str:
        pass

    @abstractmethod
    def move(self) -> str:
        pass

    @abstractmethod
    def dream(self) -> str:
        pass


class SleepState(State):

    def eat(self) -> str:
        return 'не может есть, пока спит'

    def find_food(self) -> str:
        return 'ищет еду, но только в своих мечтах'

    def move(self) -> str:
        return 'не может двигаться, пока спит'

    def dream(self) -> str:
        return 'спит и видит чудный сон'


class OnGroundState(State):

    def eat(self) -> str:
        return 'вываливает на пузо добытых моллюсков и начинает неспешно их есть'

    def find_food(self) -> str:
        return 'находит дурно пахнущую, но вполне съедобную тушу выбросившегося на берег кита'

    def move(self) -> str:
        return 'неуклюже ползет вдоль береговой линии'

    def dream(self) -> str:
        return 'на мгновние останавливается, замечтавшись об одной знакомой самке'


class InWaterState(State):

    def eat(self) -> str:
        return 'не может есть в воде'

    def find_food(self) -> str:
        return 'вспахивает бивнями морское дно, вылавливая моллюсков своими вибриссами'

    def move(self) -> str:
        return 'грациозно рассекает волны мирового океана'

    def dream(self) -> str:
        return 'не спит и не мечтает в воде - это слишком сложно'


class Walrus:

    def __init__(self, state: State) -> None:
        self._state = state

    def change_state(self, state: State) -> None:
        self._state = state

    def eat(self) -> None:
        self._execute('eat')

    def find_food(self) -> None:
        self._execute('find_food')

    def move(self) -> None:
        self._execute('move')

    def dream(self) -> None:
        self._execute('dream')

    def _execute(self, operation: str) -> None:
        try:
            func = getattr(self._state, operation)
            print('Морж {}.'.format(func()))
        except AttributeError:
            print('Морж такого делать не умеет.')


if __name__ == '__main__':
    sleep = SleepState()
    on_ground = OnGroundState()
    in_water = InWaterState()
    walrus = Walrus(on_ground)
    print('OUTPUT:')
    walrus.change_state(in_water)
    walrus.move()
    walrus.find_food()
    walrus.change_state(on_ground)
    walrus.eat()
    walrus.move()
    walrus.dream()
    walrus.change_state(sleep)
    walrus.dream()

'''
OUTPUT:
Морж грациозно рассекает волны мирового океана.
Морж вспахивает бивнями морское дно, вылавливая моллюсков своими вибриссами.
Морж вываливает на пузо добытых моллюсков и начинает неспешно их есть.
Морж неуклюже ползет вдоль береговой линии.
Морж на мгновние останавливается, замечтавшись об одной знакомой самке.
Морж спит и видит чудный сон.
'''
