"""
У нас есть завод, который производит сковородки. Он может делать 2 вида
товаров: сковорода, сковорода с крышкой
"""
from abc import ABC, abstractmethod


class Pan:
    parts: list

    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Товар: {', '.join(self.parts)}")


class Builder(ABC):
    @abstractmethod
    def produce_cap(self) -> None:
        pass

    @abstractmethod
    def produce_pan(self) -> None:
        pass


class PanBuilder(Builder):
    _pan: Pan

    def __init__(self):
        self.reset()

    @property
    def pan(self):
        pan = self._pan
        self.reset()
        return pan

    def reset(self):
        self._pan = Pan()

    def produce_cap(self) -> None:
        self._pan.add_part('крышка')

    def produce_pan(self) -> None:
        self._pan.add_part('сковорода')


class Director:
    builder: PanBuilder

    def __init__(self, builder):
        self.builder = builder

    def build_pan_with_cap(self):
        self.builder.produce_pan()
        self.builder.produce_cap()

    def build_pan(self):
        self.builder.produce_pan()


if __name__ == '__main__':
    pan_builder = PanBuilder()
    director = Director(pan_builder)
    director.build_pan()
    pan_builder.pan.list_parts()
    director.build_pan_with_cap()
    pan_builder.pan.list_parts()
