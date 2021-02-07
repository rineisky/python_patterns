handlers = []


def car_handler(func):
    handlers.append(func)
    return func


class Car:
    def __init__(self):
        self.name = None
        self.km = 11100
        self.fuel = 5
        self.oil = 5


@car_handler
def handle_fuel(car):
    if car.fuel < 10:
        print("added fuel")
        car.fuel = 100


@car_handler
def handle_km(car):
    if car.km > 10000:
        print("made a car test.")
        car.km = 0


@car_handler
def handle_oil(car):
    if car.oil < 10:
        print("Added oil")
        car.oil = 100


class Garage:
    def __init__(self, handlers=[]):
        self.handlers = handlers

    def add_handler(self, handler):
        self.handlers.append(handler)

    def handle_car(self, car):
        for handler in self.handlers:
            handler(car)


if __name__ == '__main__':
    garage = Garage(handlers)
    car = Car()
    garage.handle_car(car)
