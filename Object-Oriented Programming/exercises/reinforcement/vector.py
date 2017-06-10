from collections import Iterable

class Vector:
    def __init__(self, d):
        if isinstance(d, Iterable):
            self._coords = list(d)
        else:
            self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __sub__(self, other):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        for j in range(len(self)):
            self[j] = -self[j]
        return self

    def __mul__(self, value):
        return self._multiply(value)

    def __rmul__(self, value):
        return self._multiply(value)

    def _multiply(self, value):
        if type(value) != Vector:
            other = Vector(len(self))
            for j in range(len(self)):
                other[j] = value
        else:
            other = value
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * other[j]
        return result