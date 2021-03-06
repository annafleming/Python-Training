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
* `T.attach(p, T1, T2)` - Attach the internal structure of trees T1 and T2, respectively, as the left and right subtrees of leaf position p of T

### Array-Based Representation of a Binary Tree
An alternative representation of a binary tree T is based on a way of numbering the positions of T . 
For every position p of T , let f ( p) be the integer defined as follows.
* If p is the root of T,then f(p)=0.
* If p is the left child of position q, then f(p) = 2f(q)+1
* If p is the right child of position q, then f(p) = 2f(q)+2

#### Advantages
* One advantage of an array-based representation of a binary tree is that a position p can be represented by the single 
integer f(p), and that position-based methods such as root, parent, left, and right can be implemented using simple 
arithmetic operations on the number f(p)

#### Disadvantages
* The space usage of an array-based representation depends greatly on the shape of the tree
* Update operations for trees cannot be efficiently supported (deleting a node and promoting its child takes O(n) time).

## Tree Traversal Algorithms
A `traversal` of a tree T is a systematic way of accessing, or “visiting,” all the positions of T.

### Preorder and Postorder Traversals of General Trees - O(n)
#### Preorder traversal
The root of T is visited first and then the subtrees rooted at its children are traversed recursively.
```
Algorithm preorder(T, p):
    perform the “visit” action for position p 
    for each child c in T.children(p) do
        preorder(T, c)
```

#### Postorder traversal
Tt recursively traverses the subtrees rooted at the children of the root first, and then visits the root.
```
Algorithm preorder(T, p):
    for each child c in T.children(p) do
        preorder(T, c)
    perform the “visit” action for position p 
```

### Breadth-First Tree Traversal - O(n)
We visit all the positions at depth d before we visit the positions at depth d + 1. 
* Used in software for playing games. 
* Relies on a queue of positions to manage the traver- sal process.
```
Algorithm breadthfirst(T):
    Initialize queue Q to contain T.root() 
    while Q not empty do
        p = Q.dequeue()
        perform the “visit” action for position p 
        for each child c in T.children(p) do
            Q.enqueue(c)
```
### Inorder Traversal of a Binary Tree
We visit a position between the recursive traversals of its left and right subtrees.
```
Algorithm inorder(p):
    if p has a left child lc then
        inorder(lc)
    perform the “visit” action for position p 
    if p has a right child rc then
        inorder(rc)
```

#### Binary Search Trees
A binary search tree for S is a binary tree T such that, for each position p of T :
* Position p stores an element of S, denoted as e(p).
* Elements stored in the left subtree of p (if any) are less than e(p).
* Elements stored in the right subtree of p (if any) are greater than e(p).
* The running time of searching in a binary search tree T is proportional to the height of T

### Implementing Tree Traversals in Python
T should include support for the following methods:
* `T.positions()` - Generate an iteration of all _positions_ of tree T.
* `iter(T)` - Generate an iteration of all _elements_ stored within tree T.
```python
def __iter__(self):
    for p in self.positions():
        yield p.element() 
```
#### Preorder Traversal
```python
def preorder(self):
    if not self.is_empty():
        for p in self._subtree_preorder(self.root()): 
            yield p
def _subtree_preorder(self, p):
    yield p
    for c in self.children(p):
        for other in self._subtree_preorder(c): 
            yield other
```

#### Postorder Traversal
```python
def postorder(self):
    if not self.is_empty():
        for p in self._subtree_postorder(self.root()): 
            yield p
def _subtree_postorder(self, p):
    for c in self.children(p):
        for other in self._subtree_postorder(c): 
            yield other
    yield p
```

#### Breadth-First Traversal
```python
def breadthfirst(self):
    if not self.is_empty():
    fringe = LinkedQueue()
    fringe.enqueue(self.root())
    while not fringe.is_empty():
        p = fringe.dequeue()
        yield p
        for c in self.children(p):
            fringe.enqueue(c)
```

#### Inorder Traversal for Binary Trees
```python
def _subtree_inorder(self, p):
    if self.left(p) is not None:
        for other in self._subtree_inorder(p):
            yield other
    yield p
    if self.right(p) is not None:
        for other in self._subtree_inorder(p):
            yield other
```
### Applications of Tree Traversals
* Table of Contents
```python
def preorder_indent(T, p, d):
    print(2 * d * ' ' + str(p.element())) 
    for c in T.children(p):
        preorder_indent(T, c, d+1)
        
def preorder_label(T, p, d, path):
    label = '.'.join(str(j+1) for j in path)
    print(2 * d * ' '+ label, p.element())
    path.append(0)
    for c in T.children(p):
        preorder_label(T, c, d+1, path)
        path[−1] += 1
    path.pop()
```
* Parenthetic Representations of a Tree
* Computing Disk Space

### Euler Tours and the Template Method Pattern
The Euler tour traversal of a general tree T can be informally defined as a “walk” around T, 
where we start by going from the root toward its leftmost child, viewing the edges of T as 
being “walls” that we always keep to our left. 
```
Algorithm eulertour(T, p):
    perform the “pre visit” action for position p 
    for each child c in T.children(p) do
        eulertour(T, c)
    perform the “post visit” action for position p
```





