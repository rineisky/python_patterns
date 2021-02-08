def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Run {func.__name__}')
        result = func(*args, **kwargs)
        print(f'End {func.__name__}')
        return result

    return wrapper


def decorator_with_args(dec_arg):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            print(f'Decorator arg: {dec_arg}')
            print(f'Run {func.__name__}')
            result = func(*args, **kwargs)
            print(f'End {func.__name__}')
            return result

        return wrapper

    return inner_decorator


def class_decorator(cls):
    callable_attr = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for arg_name, arg_value in callable_attr.items():
        decorated = decorator(arg_value)
        setattr(cls, arg_name, decorated)
    return cls


@class_decorator
class SomeClass:
    def __init__(self):
        self.a = 'a'

    def print_a_with_b(self, b):
        print(f'{self.a} with {b}')


sc = SomeClass()
sc.print_a_with_b('b')
