from .ll_node import Node


class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head.element

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._head.element
        self._head = self._head.next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail.next = newest
        self._tail = newest
        self._size += 1

    def __iter__(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        cursor = self._head
        for i in range(len(self)):
            yield cursor.element
            cursor = cursor.next

    def get_last_element(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        for index, node in enumerate(self):
            if index == len(self) - 1:
                return node

    def get_first_node(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head

    def _count_nodes(self, root_node):
        if root_node is None:
            return 0
        else:
            return 1 + self._count_nodes(root_node.next)





