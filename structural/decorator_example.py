from abc import ABCMeta, abstractmethod


class IOperator(metaclass=ABCMeta):
    @abstractmethod
    def operator(self):
        pass


class Component(IOperator):
    def operator(self):
        return 10.0


class Wrapper(IOperator):
    def __init__(self, obj):
        self.obj = obj

    def operator(self):
        return self.obj.operator() + 5.0


comp = Component()
comp = Wrapper(comp)
print(comp.operator())
