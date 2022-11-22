import math


class Vector(object):
    CANNOT_NORMALIZE_ERR_MSG = 'ERR: Zero vector cannot be normalized'
    CANNOT_COMPUTE_ANGLE = 'ERR: Cannot compute an angle with a zero vector'

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

    def scalar_product(self, c):
        new_v = [c * x for x in self.coordinates]
        return Vector(new_v)

    def magnitude(self):
        return math.sqrt(sum([math.pow(x, 2) for x in self.coordinates]))

    def normalized(self):
        try:
            return self.scalar_product(1.0 / self.magnitude())
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ERR_MSG)

    def dot_product(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            in_rads = math.acos(u1.dot_product(u2))

            return in_rads * (180.0 / math.pi) if in_degrees else in_rads

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ERR_MSG:
                raise Exception(self.CANNOT_COMPUTE_ANGLE)
            else:
                raise e

