from math import *
from decimal import Decimal, getcontext


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


class Vector(object):
    CANNOT_NORMALIZE_ERR_MSG = 'ERR: Zero vector cannot be normalized'
    CANNOT_COMPUTE_ANGLE_MSG = 'ERR: Cannot compute an angle with a zero vector'
    CANNOT_FIND_UNIQUE_PARALLEL_COMP_MSG = 'ERR: Cannot find a unique parallel component'
    CANNOT_FIND_UNIQUE_ORTHOGONAL_COMP_MSG = 'ERR: Cannot find a unique orthogonal component'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(c) for c in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('ERR: The coordinates must be nonempty')

        except TypeError:
            raise TypeError('ERR: The coordinates must be an iterable')

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current >= len(self.coordinates):
            raise StopIteration
        else:
            current_value = self.coordinates[self.current]
            self.current += 1
            return current_value

    def next(self):
        return self.__next__()

    def __len__(self):
        return len(self.coordinates)

    def __getitem__(self, i):
        return self.coordinates[i]

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
        return Vector([Decimal(c) * coord for coord in self.coordinates])

    def magnitude(self):
        return Decimal(sqrt(sum([coord * coord for coord in self.coordinates])))

    def normalize(self):
        try:
            return self.scalar_product(Decimal('1.0') / self.magnitude())
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ERR_MSG)

    def dot_product(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalize()
            u2 = v.normalize()
            in_rads = acos(u1.dot_product(u2))

            return in_rads * (180.0 / pi) if in_degrees else in_rads

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ERR_MSG:
                raise Exception(self.CANNOT_COMPUTE_ANGLE_MSG)
            else:
                raise e

    def is_zero(self):
        return set(self.coordinates) == {Decimal(0)}

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot_product(v)) < tolerance

    def is_parallel_to(self, v):
        return (
                self.is_zero() or
                v.is_zero() or
                self.angle_with(v) == 0 or
                self.angle_with(v) == pi
        )

    def component_parallel_to(self, basis_v):
        try:
            basis_u = basis_v.normalize()
            mag = self.dot_product(basis_u)
            return basis_u.scalar_product(mag)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ERR_MSG:
                raise Exception(self.CANNOT_FIND_UNIQUE_PARALLEL_COMP_MSG)
            else:
                raise e

    def component_orthogonal_to(self, basis_v):
        try:
            projection = self.component_parallel_to(basis_v)
            return self - projection

        except Exception as e:
            if str(e) == self.CANNOT_FIND_UNIQUE_PARALLEL_COMP_MSG:
                raise Exception(self.CANNOT_FIND_UNIQUE_ORTHOGONAL_COMP_MSG)
            else:
                raise e

    def cross_product(self, v):
        if self.dimension == 2 and v.dimension == 2:
            return Vector([0.,
                           0.,
                           (self.coordinates[0] * v.coordinates[1] - self.coordinates[1] * v.coordinates[0])])
        elif self.dimension == 3 and v.dimension == 3:
            return Vector([(self.coordinates[1] * v.coordinates[2] - self.coordinates[2] * v.coordinates[1]),
                           (self.coordinates[2] * v.coordinates[0] - self.coordinates[0] * v.coordinates[2]),
                           (self.coordinates[0] * v.coordinates[1] - self.coordinates[1] * v.coordinates[0])])
        else:
            return Vector([0., 0., 0.])

    def area_of_parallelogram_with(self, v):
        return self.cross_product(v).magnitude()

    def area_of_triangle_with(self, v):
        return self.area_of_parallelogram_with(v) / 2
