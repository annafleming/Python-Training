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