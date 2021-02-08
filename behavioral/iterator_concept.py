from collections.abc import Iterable, Iterator
from typing import Any, List


class AlphabeticalOrderIterator(Iterator):
    """
    Конкретные Итераторы реализуют различные алгоритмы обхода. Эти классы
    постоянно хранят текущее положение обхода.
    """
    _position: int = None
    _reverse: bool = False

    def __init__(self, sequence, reverse=False) -> None:
        self._sequence = sequence
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        Метод __next __() должен вернуть следующий элемент в последовательности.
        При достижении конца коллекции и в последующих вызовах должно вызываться
        исключение StopIteration.
        """
        try:
            value = self._sequence[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


class WordsCollection(Iterable):
    """
    Конкретные Коллекции предоставляют один или несколько методов для получения
    новых экземпляров итератора, совместимых с классом коллекции.
    """

    def __init__(self, sequence: List[Any] = None) -> None:
        self._sequence = [] if sequence is None else sequence

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._sequence)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._sequence, True)

    def add_item(self, item: Any):
        self._sequence.append(item)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print('\n')
    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()))
