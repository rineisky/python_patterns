from abc import ABC, abstractmethod


class ToolBase(ABC):
    @abstractmethod
    def write(self, name, text):
        pass


class PenTool(ToolBase):
    def write(self, name, text):
        print(f'{name} (ручкой) {text}')


class BrushTool(ToolBase):
    def write(self, name, text):
        print(f'{name} (кистью) {text}')


class People:
    tool: ToolBase

    def __init__(self, name, tool):
        self.name = name
        self.tool = tool

    def set_tool(self, tool):
        self.tool = tool

    def write(self, text):
        self.tool.write(self.name, text)


class Student(People):
    def __init__(self, name):
        super().__init__(name, PenTool())


class Painter(People):
    def __init__(self, name):
        super().__init__(name, BrushTool())


if __name__ == '__main__':
    maxim = Student('Максим')
    maxim.write('Пишу лекцию о паттерне Стратегия')

    sasha = Painter('Саша')
    sasha.write('Рисую иллюстрацию к паттерну Стратегия')

    sasha.set_tool(PenTool())
    sasha.write('Нет, уж лучше я напишу конспект')
