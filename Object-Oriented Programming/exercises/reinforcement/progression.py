class Progression:
    def __init__(self, start=0):
        self._current = start

    def advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self.advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self.increment = increment

    def advance(self):
        self._current += self.increment


class GeometricProgression(Progression):
    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def advance(self):
        self._current = self._base


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def advance(self):
        self._prev, self._current = self._current, self._prev + self._current

    def get_element_by_position(self, position):
        for i in range(position-1):
            self.advance()
        return self._current


class DiffProgression(Progression):
    def __init__(self, first, second):
        super().__init__(second)
        self._prev = first

    def advance(self):
        self._prev, self._current = self._current, abs(self._prev - self._current)

    def get_current(self):
        return self._current