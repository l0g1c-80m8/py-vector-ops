import math
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('ERR: The coordinates must be nonempty')

        except TypeError:
            raise TypeError('ERR: The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        new_v = [c1 + c2 for c1, c2 in zip(self.coordinates, v.coordinates)]
        return Vector(new_v)

    def __sub__(self, v):
        new_v = [c1 - c2 for c1, c2 in zip(self.coordinates, v.coordinates)]
        return Vector(new_v)

    def product_scalar(self, c):
        new_v = [c * x for x in self.coordinates]
        return Vector(new_v)

    def magnitude(self):
        return math.sqrt(sum([math.pow(x, 2) for x in self.coordinates]))

    def normalized(self):
        try:
            return self.product_scalar(1.0 / self.magnitude())
        except ZeroDivisionError:
            raise Exception('ERR: Zero vector cannot be normalized')

