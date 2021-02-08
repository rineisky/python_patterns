import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Coord:
    x: int
    y: int
    z: int

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x} {self.y} {self.z}'


if __name__ == '__main__':
    a = Coord(2, 1, 5)
    prototype = Prototype()
    prototype.register_object('point_a', a)
    b = prototype.clone('point_a')
    c = prototype.clone('point_a', x=1, y=2, comment='point_c')
    print([str(i) for i in (a, b, c)])
    print(c.comment)
