## The Priority Queue Abstract Data Type
### Priorities
This is a collection of prioritized elements that allows arbitrary element insertion, and allows the removal of the element that has first priority.
### The Priority Queue ADT
* `P.add(k, v)` - Insert an item with key k and value v into priority queue P.
* `P.min()` - Return a tuple, (k,v), representing the key and value of an item in priority queue P with minimum key
* `P.remove_min()`
* `P.is_empty()`
* `len(P)`

## Heaps
### The Heap Data Structure
* `Heap-Order Property` - In a heap T, for every position p other than the root, the key stored at p is greater than or equal to the key stored at p’s parent.
* `Complete Binary Tree Property` - A heap T with height h is a complete binary tree if levels 0,1,2,...,h−1 of T have the maximum number of nodes possible 
(namely, level i has 2i nodes, for 0 ≤ i ≤ h − 1) and the remaining nodes at level h reside in the leftmost possible positions at that level.
* A heap T storing n entries has height `h = ⌊log n⌋`.

### Implementing a Priority Queue with a Heap
#### Adding an Item to the Heap
* The new node should be placed at a position p just beyond the rightmost node at the bottom level of the tree, 
or as the leftmost position of a new level, if the bottom level is already full (or if the heap is empty).
* Up-Heap Bubbling After an Insertion

#### Removing the Item with Minimum Key
* Remove root
* Move the leaf at the last position p of T to the root
* Down-Heap Bubbling After a Removal (choosing a child of p with minimal key.)

#### Array-Based Representation of a Complete Binary Tree
* If p is the root of T,then f(p)=0.
* If p is the left child of position q, then f(p) = 2f(q)+1.
* If p is the right child of position q, then f(p) = 2f(q)+2.

### Python’s heapq Module
* `heappush(L, e)` - Push element e onto list L and restore the heap-order property.
* `heappop(L)` - Pop and return the element with smallest value from list L, and reestablish the heap-order property.
* `heappushpop(L, e)` - Push element e on list L and then pop and return the smallest item.
* `heapreplace(L, e)`
* `heapify(L)`
* `nlargest(k, iterable)`
* `nsmallest(k, iterable)`

## Sorting with a Priority Queue
### Selection-Sort and Insertion-Sort
* `Selection-Sort` - using Unsorted Priority Queue, the bottleneck computation is the repeated “selection” of the minimum element - O(n2)
* `Insertion-Sort` - using  Sorted Priority Queue, the bottleneck computation is adding the items - O(n2)

### Heap-Sort
O(n log n)

## Adaptable Priority Queues
* `P.update(loc, k, v)` - Replace key and value for the item identified by locator `loc`.
* `P.remove(loc)` - Remove the item identified by locator `loc` from the priority
queue and return its (key,value) pair.