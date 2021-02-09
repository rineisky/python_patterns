import copy


class Prototype:
    """
    Класс прототипа, который будет хранить все зарегистрированные прототипы
    и делать их копии
    """
    _objects: dict

    def __init__(self):
        self._objects = {}

    def register(self, name, new_prototype):
        """
        Регистрируем новый прототип, чтобы потом его копировать
        """
        self._objects[name] = new_prototype

    def unregister(self, name):
        """
        Удаляем зарегистрированный прототип
        """
        self._objects.pop(name)

    def clone(self, name, **new_attr):
        """
        Клонирование прототипа с возможностью переопределения атрибутов
        """
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(new_attr)
        return obj


class CircularReference:
    """
    Класс, объект которого будет имитировать механизм циклических ссылок
    """
    link: 'Component'

    def set_link(self, component: 'Component'):
        self.link = component


class Component:
    """
    Класс, который содержит атрибуты с изменяемыми и неизменяемыми типами данных
    """

    def __init__(self, immutable, mutable, circular_reference):
        """
        В Python неизменяемые значения передаются по значению, а изменяемые по ссылке
        Объект некоторого другого класса также передается по ссылке, так что его можно
        считать mutable

        :param immutable: параметр неизменяемого типа данных
        :param mutable: параметр изменяемого типа данных
        :param circular_reference: параметр, который будет содержать циклическую ссылку
        """
        self.immutable = immutable
        self.mutable = mutable
        self.circular_reference = circular_reference

    # Если хотим переопределить механизм поверхностного копирования
    # def __copy__(self):
    #     pass

    # Если хотим переопределить механизм глубокого копирования
    # def __deepcopy__(self):
    #     pass


if __name__ == "__main__":
    prototype_obj = Prototype()

    mutable_data = [1, 2, 3, {'a': 2}]
    circular_ref = CircularReference()
    component_obj = Component('immutable', mutable_data, circular_ref)

    prototype_obj.register('obj', component_obj)
    cloned_obj = prototype_obj.clone('obj')

    if cloned_obj is not component_obj:
        print('клонирование прошло успешно')
    print(f"Исходный объект ({id(component_obj):X}): {vars(component_obj)}")
    print(f"Объект-клон ({id(cloned_obj):X}): {vars(cloned_obj)}")
