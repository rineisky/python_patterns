from abc import ABCMeta, abstractmethod


class IOperator(object):
    """
    Интерфейс, который должны реализовать как декоратор,
    так и оборачиваемый объект.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def operator(self):
        pass


class Component(IOperator):
    """Компонент программы"""

    def operator(self):
        return 10.0


class Wrapper(IOperator):
    """Декоратор"""

    def __init__(self, obj):
        self.obj = obj

    def operator(self):
        return self.obj.operator() + 5.0


comp = Component()
comp = Wrapper(comp)
print(comp.operator())
# 15.0
