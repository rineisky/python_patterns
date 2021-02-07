from abc import ABCMeta, abstractmethod


class Iterator(metaclass=ABCMeta):
    """
    Абстрактный итератор
    """

    _error = None  # класс ошибки, которая прокидывается в случае выхода за границы коллекции

    def __init__(self, collection, cursor):
        """
        Constructor.

        :param collection: коллекция, по которой производится проход итератором
        :param cursor: изначальное положение курсора в коллекции (ключ)
        """
        self._collection = collection
        self._cursor = cursor

    @abstractmethod
    def current(self):
        """
        Вернуть текущий элемент, на который указывает итератор
        """
        pass

    @abstractmethod
    def next(self):
        """
        Сдвинуть курсор на следующий элемент коллекции и вернуть его
        """
        pass

    @abstractmethod
    def has_next(self):
        """
        Проверить, существует ли следующий элемент коллекции
        """
        pass

    @abstractmethod
    def remove(self):
        """
        Удалить текущий элемент коллекции, на который указывает курсор
        """
        pass

    def _raise_key_exception(self):
        """
        Прокинуть ошибку, связанную с невалидным индексом, содержащимся в курсоре
        """
        raise self._error('Collection of class {} does not have key "{}"'.format(
            self.__class__.__name__, self._cursor))


class ListIterator(Iterator):
    """
    Итератор, проходящий по обычному списку
    """

    _error = IndexError

    def __init__(self, collection: list):
        super().__init__(collection, 0)

    def current(self):
        if self._cursor < len(self._collection):
            return self._collection[self._cursor]
        self._raise_key_exception()

    def next(self):
        if len(self._collection) >= self._cursor + 1:
            self._cursor += 1
            return self._collection[self._cursor]
        self._raise_key_exception()

    def has_next(self):
        return len(self._collection) >= self._cursor + 1

    def remove(self):
        if 0 <= self._cursor < len(self._collection):
            self._collection.remove(self._collection[self._cursor])
        else:
            self._raise_key_exception()


class DictIterator(Iterator):
    """
    Итератор, проходящий по словарю - из-за того, что словари в Python'е реализованы,
    как хеш-таблицы, порядок обхода может меняться во время разных запусков
    """

    _error = KeyError

    def __init__(self, collection: dict):
        super().__init__(collection, next(iter(collection)))
        self._keys = list(self._collection.keys())
        self._keys.pop(0)

    def current(self):
        if self._cursor in self._collection:
            return self._collection[self._cursor]
        self._raise_key_exception()

    def next(self):
        if len(self._keys):
            self._cursor = self._keys.pop(0)
            return self._collection[self._cursor]
        else:
            self._raise_key_exception()

    def has_next(self):
        return len(self._keys) > 0

    def remove(self):
        if self._cursor in self._collection:
            del self._collection[self._cursor]
            try:
                self.next()
            except self._error:
                raise KeyError('Collection of type {} is empty'.format(self.__class__.__name__))
        else:
            self._raise_key_exception()


class Collection(metaclass=ABCMeta):
    """
    Абстрактная коллекция
    """

    @abstractmethod
    def iterator(self):
        pass


class ListCollection(Collection):
    """
    Коллекция-обертка для обычного списка
    """

    def __init__(self, collection: list):
        self._collection = collection

    def iterator(self):
        return ListIterator(self._collection)


class DictCollection(Collection):
    """
    Коллекция-обертка для словаря
    """

    def __init__(self, collection: dict):
        self._collection = collection

    def iterator(self):
        return DictIterator(self._collection)


def test(title=str, collection=Collection):
    print("\n{}\n".format(title))
    iterator = collection.iterator()
    print(iterator.current())
    iterator.next()
    print(iterator.next())
    iterator.remove()
    print(iterator.current())
    print(iterator.has_next())
    print()


if __name__ == '__main__':
    print('OUTPUT:')
    test('List testing', ListCollection([1, 2, 3, 4, 5]))
    test('Dictionary testing', DictCollection({'a': 1, 'b': 2, 'c': 3, 'f': 8}))

'''
OUTPUT:

List testing

1
3
4
True


Dictionary testing

1
3
2
False
'''