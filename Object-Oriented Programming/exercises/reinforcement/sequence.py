from abc import ABCMeta, abstractmethod
class Sequence(metaclass=ABCMeta):

    @abstractmethod
    def len(self):

    @abstractmethod
    def getitem(self, j):

    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')

    def count(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return k

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i in len(self):
            if self[i] != other[i]:
                return False
        return True

    def __lt__(self, other):
        min_length = len(self) if len(self) < len(other) else other
        for i in range(min_length):
            if self[i] < other[i]:
                return True
            elif self[i] > other[i]:
                return False

        return True if len(self) < len(other) else False


class SequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        return self

class ReversedSequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = len(self._seq) - 1

    def __next__(self):
        self._k -= 1
        if self._k >=0
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        return self
