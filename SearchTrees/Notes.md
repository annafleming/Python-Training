## Binary Search Trees
A binary search tree is a binary tree T with each position p storing a key-value pair (k,v) such that:
* Keys stored in the left subtree of p are less than k.
* Keys stored in the right subtree of p are greater than k.
An `inorder traversal` of a binary search tree visits positions in increasing order of their keys.

### Searches O(h)
```
    Algorithm TreeSearch(T, p, k):
        if k == p.key() then 
            return p                                        {successful search} 
        else if k < p.key() and T.left(p) is not None then 
            return TreeSearch(T, T.left(p), k)              {recur on left subtree}
        else if k > p.key() and T.right(p) is not None then 
            return TreeSearch(T, T.right(p), k)             {recur on right subtree}
        return p                                            {unsuccessful search}
```

### Insertion
```
    Algorithm TreeInsert(T, k, v):
        Input: A search key k to be associated with value v
        p = TreeSearch(T,T.root(),k) 
        if k == p.key() then
            Set p’s value to v 
        else if k < p.key() then
            add node with item (k,v) as left child of p 
        else
            add node with item (k,v) as right child of p
```


