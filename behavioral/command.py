from abc import ABCMeta, abstractmethod


class Troop:
    """
    Receiver - объект военного отряда
    """

    def move(self, direction: str) -> None:
        """
        Начать движение в определенном направлении
        """
        print('Отряд начал движение {}'.format(direction))

    def stop(self) -> None:
        """
        Остановиться
        """
        print('Отряд остановился')


class Command(metaclass=ABCMeta):
    """
    Базовый класс для всех команд
    """

    @abstractmethod
    def execute(self) -> None:
        """
        Приступить к выполнению команды
        """
        pass

    @abstractmethod
    def unexecute(self) -> None:
        """
        Отменить выполнение команды
        """
        pass


class AttackCommand(Command):
    """
    Команда для выплнения атаки
    """

    def __init__(self, troop: Troop) -> None:
        """
        Constructor.

        :param troop: отряд, с которым ассоциируется команда
        """
        self.troop = troop

    def execute(self) -> None:
        self.troop.move('вперед')

    def unexecute(self) -> None:
        self.troop.stop()


class RetreatCommand(Command):
    """
    Команда для выполнения отступления
    """

    def __init__(self, troop: Troop) -> None:
        """
        Constructor.

        :param troop: отряд, с которым ассоциируется команда
        """
        self.troop = troop

    def execute(self) -> None:
        self.troop.move('назад')

    def unexecute(self) -> None:
        self.troop.stop()


class TroopInterface:
    """
    Invoker - интерфейс, через который можно отдать команды определенному отряду
    """

    def __init__(self, attack: AttackCommand, retreat: RetreatCommand) -> None:
        """
        Constructor.

        :param attack: команда для выполнения атаки
        :param retreat: команда для выполнения отступления
        """
        self.attack_command = attack
        self.retreat_command = retreat
        self.current_command = None  # команда, выполняющаяся в данный момент

    def attack(self) -> None:
        self.current_command = self.attack_command
        self.attack_command.execute()

    def retreat(self) -> None:
        self.current_command = self.retreat_command
        self.retreat_command.execute()

    def stop(self) -> None:
        if self.current_command:
            self.current_command.unexecute()
            self.current_command = None
        else:
            print('Отряд не может остановиться, так как не двигается')


if __name__ == '__main__':
    troop = Troop()
    interface = TroopInterface(AttackCommand(troop), RetreatCommand(troop))
    interface.attack()
    interface.stop()
    interface.retreat()
    interface.stop()