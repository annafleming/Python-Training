## Singly Linked Lists

A `singly linked list`, in its simplest form, is a collection of `nodes` that collectively form a linear sequence. 
Each node stores a reference to an object that is an element of the sequence, as well as a reference to the next node of the list.

* First node - `head`
* Last node - `tail` (reference = None)

## Circularly Linked Lists

### Round-Robin Schedulers
It iterates through a collection of elements in a circular fashion and “services” each element 
by performing a given action on it(used to allocate slices of CPU time).
1. e = Q.dequeue() 
2. Service element `e`
3. Q.enqueue(e)

## Doubly Linked Lists
A linked list in which each node keeps an explicit reference to the node before it and a reference to the node after it.

“Dummy” nodes also known as `sentinels` (or guards)
* `header`
* `trailer`

## The Positional List ADT

### The Positional List Abstract Data Type

#### Position ADT
* `p.element()` - Return the element stored at position `p`.

#### Positional list ADT
* `L.first()` - position of the first element
* `L.last()`
* `L.before(p)`
* `L.after(p)`
* `L.is_empty( )`
* `len(L)`
* `iter(L)` - Return a forward iterator for the elements of the list
* `L.add_first(e)`
* `L.add_last(e)`
* `L.add_before(p, e)`
* `L.add_after(p, e)`
* `L.replace(p, e)`
* `L.delete(p)`

## Sorting a Positional List

```python
def insertion_sort(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() < value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)
```

## Case Study: Maintaining Access Frequencies
Collection of elements while keeping track of the number of times each element is accessed.
### Favorites list ADT
* `access(e)`
* `remove(e)`
* `top(k)`

## Move-to-Front Heuristic
Each time we access an element we move it all the way to the front of the list.

## Link-Based vs. Array-Based Sequences
### Advantages of Array-Based Sequences
* Arrays provide O(1)-time access to an element based on an integer index. (`vs. O(k) in linked list`)
* Operations with equivalent asymptotic bounds typically run a constant 
factor more efficiently with an array-based structure versus a linked structure. 
(instantiating and linking nodes in LinkedList)
* Array-based representations typically use proportionally less memory than linked structures.
### Advantages of Link-Based Sequences
* Link-based structures provide worst-case time bounds for their operations.
* Link-based structures support O(1)-time insertions and deletions at arbi- trary positions.
