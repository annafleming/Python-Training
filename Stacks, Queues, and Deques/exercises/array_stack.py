from .custom_exceptions import Empty,Full


class ArrayStack:
    def __init__(self, capacity=-1):
        self.data = []
        self.capacity = capacity

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        if len(self) == self.capacity:
            raise Full('Stack capacity is exceeded')

        self.data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data.pop()
