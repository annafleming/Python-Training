from .custom_exceptions import Empty

class ArrayDeque:
    DEFAULT_CAPACITY = 2

    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        return self._data[self._front]

    def last(self):
        index = (self._front + self._size - 1) % len(self._data)
        return self._data[index]

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)
        avail = (self._front - 1) % len(self._data)
        self._data[avail] = e
        self._size += 1
        self._front = avail

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def delete_first(self):
        answer = self.first()
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def delete_last(self):
        index = (self._front + self._size - 1) % len(self._data)
        answer = self.last()
        self._data[index] = None
        self._size -= 1
        return answer

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0


