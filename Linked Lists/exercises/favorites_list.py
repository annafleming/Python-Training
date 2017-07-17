from .positional_list import PositionalList

class FavoritesList:
    __slots__ = '_value', '_count'

    class Item:
        def __init__(self, e):
            self._value = e
            self._count = 0

    def _find_position(self, e):
        walk = self._data.first()
        while walk is not None and e != walk.element()._value:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while walk != self._data.first() and cnt > self._data.before(walk).element()._count:
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, e):
        pass

    def remove(self, e):
        pass

    def top(self, k):
        pass
