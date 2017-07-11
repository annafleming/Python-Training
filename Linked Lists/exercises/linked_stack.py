from .ll_node import Node


class LinkedStack:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = Node(e, self._head)
        self._size +=1

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head.element

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        answer = self._head.element
        self._head = self._head.next
        self._size -= 1
        return answer