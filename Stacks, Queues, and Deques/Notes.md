## Stacks
A `stack` is a collection of objects that are inserted and removed according 
to the `last-in, first-out (LIFO) principle`.
 Formally, a stack is an `abstract data type (ADT)` such that an instance `S` supports the following two methods:
* `S.push(e)`
* `S.pop()`
* `S.top()`
* `S.is_empty()`
* `len(S)`
### An Algorithm for Matching Delimiters
```python
def is_matched(expr):
    lefty = '({[' 
    righty = ')}]'
    S = ArrayStack() 
    for c in expr:
        if c in lefty: 
            S.push(c)
        elif c in righty:
            if S.is_empty(): 
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()
```

## Queues
Queue is a collection of objects that are inserted and removed according to the 
`first-in, first-out (FIFO)` principle.
The queue abstract data type (ADT) supports the following two fundamental methods for a queue Q:
* `Q.enqueue(e)`
* `Q.dequeue()`
* `Q.first()`
* `Q.is_empty()`
* `len(Q)`

## Double-Ended Queues
A queue-like data structure that supports insertion and deletion at both the front and the back of the queue.