## Maps and Dictionaries
### The Map ADT
* `M[k]`
* `M[k] = v`
* `del M[k]`
* `len(M)`
* `iter(M)`
* `k in M`
* `M.get(k, d=None)` - Return M[k] if key k exists in the map; otherwise return default value d.
* `M.setdefault(k, d)` - If key k exists in the map, simply return M[k]; if key k does not exist, set M[k] = d and return that value.
* `M.pop(k, d=None)`
* `M.popitem()` - Remove an arbitrary key-value pair from the map
* `M.clear()`
* `M.keys()`
* `M.values()`
* `M.items()` - Return a set-like view of (k,v) tuples for all entries of M.
* `M.update(M2)` - Assign M[k] = v for every (k,v) pair in map M2.
* `M == M2`
* `M != M2`

#### Mapping(python class)
* `pop`
* `popitem`
* `clear`
* `update`
* `setdefault`

#### MutableMapping(python class)
* `__getitem__`
* `__setitem__`
* `__delitem__`
* `__len__`
* `insert`

## Hash Tables
### Hash Functions
The goal of a `hash function`, h, is to map each key k to an integer in the range [0, N − 1], where N is the capacity of the bucket array for a hash table.
We say that a hash function is “good” if it maps the keys in our map so as to sufficiently minimize `collisions`.

#### It is common to view the evaluation of a hash function, h(k), as consisting of two portions
* a `hash code` that maps a key k to an integer
* and a `compression function` that maps the hash code to an integer within a range of indices, [0, N − 1], for a bucket array.

`hash(x)` - works with immutable types: `int`, `float`, `str`, `tuple`, and `frozenset`

#### Compression Functions
* The Division Method
`i mod N` - Choosing N to be a prime number helps to reduce collisions
* The MAD Method - Multiply-Add-and-Divide

### Collision-Handling Schemes
* Separate Chaining
Each bucket A[j] stores its own secondary container, holding items (k, v) such that h(k) = j
* Open Addressing
* Linear Probing and Its Variants

## Sorted Maps
* `M.find_min()`
* `M.find_max()`
* `M.find_lt(k)` - less than k
* `M.find_le(k)` - less than or equal to k
* `M.find_gt(k)`
* `M.find_ge(k)`
* `M.find_range(start, stop)` - Iterate all (key,value) pairs with start <= key < stop.
* `iter(M)`
* `reversed(M)`

## Skip Lists
A skip list S for a map M consists of a series of lists {S0,S1,...,Sh}. 
Each list Si stores a subset of the items of M sorted by increasing keys, plus items with two sentinel keys denoted −∞ and +∞, 
where −∞ is smaller than every possible key that can be inserted in M and +∞ is larger than every possible key that can be inserted in M. 
In addition, the lists in S satisfy the following:
• List S0 contains every item of the map M (plus sentinels −∞ and +∞).
• For i = 1,...,h−1, list Si contains (in addition to −∞ and +∞) a randomly
generated subset of the items in list Si−1. 
• List Sh contains only −∞ and +∞.

The positions in a skip list can be traversed using the following operations:
* `next(p)` - Return the position following p on the same level.
* `prev(p)` - Return the position preceding p on the same level.
* `below(p)` - Return the position below p in the same tower.
* `above(p)` - Return the position above p in the same tower.

### Searching in a Skip List
```
    Algorithm SkipSearch(k):
        Input: A search key k
        Output: Position p in the bottom list S0, with the largest key such that key(p) <= k
        p = start
        while below(p) != None do
            p = below(p)
            while k >= key(next(p)) do
                p = next(p)
        return p
```

## Sets, Multisets, and Multimaps
A __set__ is an unordered collection of elements, without duplicates, that typically supports efficient membership tests. 
In essence, elements of a set are like keys of a map, but without any auxiliary values.
A __multiset__(also known as a __bag__)is a set-like container that allows duplicates.
A __multimap__ is similar to a traditional map, in that it associates values with keys; however, in a multimap the same key can be mapped to multiple values.