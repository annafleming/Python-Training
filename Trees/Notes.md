## General Trees
### Tree Definitions and Properties
* A `tree` is an abstract data type that stores elements hierarchically.
* With the exception of the top element, each element in a tree has a `parent `
element and zero or more `children` elements.
* We typically call the top element the `root`.
* Two nodes that are children of the same parent are `siblings`.
* A node v is `external` if v has no children, also known as `leaves`.
* A node v is `internal` if it has one or more children. 
* An `edge` of tree T is a pair of nodes (u,v) such that u is the parent of v, or vice versa.
* A `path` of T is a sequence of nodes such that any two consecutive nodes in the sequence form an edge.
* A tree is `ordered` if there is a meaningful linear order among the children of each node.

### The Tree Abstract Data Type
* `p.element()` - Return the element stored at position p.
* `T.root()` - Return the position of the root of tree T, or None if T is empty.
* `T.is_root(p)`
* `T.parent(p)` - Return the position of the parent of position p, or None if p is the root of T.
* `T.num children(p)`
* `T.children(p)` - Generate an iteration of the children of position p.
* `T.is_leaf(p)`
* `len(T)`
* `T.is_empty()`
* `T.positions()` - Generate an iteration of all positions of tree T.
* `iter(T)` - Generate an iteration of all elements stored within tree T.

#### Height





