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
The height of a nonempty tree T is equal to the maximum of the depths of its leaf positions.
```python
def height(self, p):
    if self.is_leaf(p):
        return 0 
    else:
        return 1 + max(self.height(c) for c in self.children(p))
```

## Binary Trees
A `binary tree` is an ordered tree with the following properties:
* Every node has at most two children.
* Each child node is labeled as being either a `left child` or a `right child`.
* A left child precedes a right child in the order of children of a node.
* A binary tree is `proper` if each node has either zero or two children.
* Also known as `decision trees`.

### The Binary Tree Abstract Data Type
* `T.left(p)` - Return the position that represents the left child of p, or None if p has no left child.
* `T.right(p)`
* `T.sibling(p)`

### Properties of Binary Trees
* In general, level d has at most 2^d nodes.
* nE = nI + 1

## Implementing Trees
* `T.add_root(e)`
* `T.add_left(p, e)` - Create a new node storing element e, link the node as the left child of position p
* `T.add_right(p, e)`
* `T.replace(p, e)` - Replace the element stored at position p with element e, and return the previously stored element.
* `T.delete(p)` - Remove the node at position p, replacing it with its child, if any.
* `T.attach(p, T1, T2)` - Attach the internal structure of trees T1 and T2, respec- tively, as the left and right subtrees of leaf position p of T










