from .ll_node import Node


class CircularQueue:
    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._tail.next.element

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        old_head = self._tail.next
        if self._size == 1:
            self._tail = 0
        else:
            self._tail.next = old_head.next
        self._size -= 1
        return old_head.element

    def enqueue(self, e):
        newest = Node(e, None)
        if self.is_empty():
            newest.next = newest
        else:
            newest.next = self._tail.next
            self._tail.next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self.size > 0:
            self._tail = self._tail.next

    def count_nodes(self):
        if self.is_empty():
            return 0
        count = 1
        walk = self._tail.next
        while walk != self._tail:
            count += 1
            walk = walk.next
        return count

