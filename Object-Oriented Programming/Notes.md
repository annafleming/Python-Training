## Abstract Base Classes

from abc import ABCMeta, abstractmethod
`@abstractmethod` decorator

## Instance and Class Namespaces
The special attribute `__slots__` allows you to explicitly state which instance attributes you expect your object instances to have, with the expected results:
* faster attribute access.
* space savings in memory.

## Shallow and Deep Copying

* shallow copy -  the new list represents a sequence of references to the same elements as in the first.
```python 
palette = list(warmtones)
```

* deep copy - copy Module
```python 
palette = copy.deepcopy(warmtones)```