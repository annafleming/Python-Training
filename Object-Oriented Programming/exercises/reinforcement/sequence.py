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
