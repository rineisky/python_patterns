"""
Синглтон через декоратор
"""


def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance


@singleton
class MyClass:
    pass


if __name__ == '__main__':
    first_obj = MyClass()
    second_obj = MyClass()
    print(f'Переменные ссылаются на один объект: {first_obj is second_obj}')
