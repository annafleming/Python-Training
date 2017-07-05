## Low-Level Arrays
A group of related variables can be stored one after another in a contiguous portion of the computer’s memory. 
We will denote such a representation as an _array_.
Each cell of an array must use the same number of bytes.

### Referential Arrays
Python represents a list or tuple instance using an internal storage mechanism of an array of object _references_.

* ```counters = [0] * 8``` - all 8 elements of the array point at the same memory cell
* ```primes.extend(extras)``` - extended list does not receive copies of those elements, it receives references to those elements

### Compact Arrays in Python
Array is storing the bits that represent the primary data (characters, in the case of strings), not references.

#### Advantages
* Lower overall memory usage (no need to store memory references - normally 64-bits)
* Primary data are stored consecutively in memory. Because of the workings of the cache and memory hierarchies of computers, it is often advantageous to have data stored in memory near other data that might be used in the same computations.

Primary support for compact arrays is in a module named __array__
```primes = array( 'i' , [2, 3, 5, 7, 11, 13, 17, 19])``` - 'i' (signed int)

##Dynamic Arrays and Amortization
Python’s list class relies on a `dynamic array`. 
Allocates initially more memory than need. Migrates to the new larger array as needed.

## Efficiency of Python’s Sequence Types
### Python’s List and Tuple Classes
##### Nonmutating behaviors
k - leftmost occurrence
* `len(data)` - O(1)
* `data[j]` - O(1)
* `data.count(value)` - O(n)
* `data.index(value)` - O(k+1)
* `value in data` - O(k+1)
* `data1 == data2` - O(k+1)
* `data[j:k]` - O(k+1)
* `data1 + data2` - O(n1+n2)
* `c * data` - O(c*n)

##### Mutating behaviors
* `data[j] = val` - O(1)
* `data.append(value)` - O(1)∗
* `data.insert(k, value)` - O(n−k+1)∗
* `data.pop()` - O(1)∗
* `data.pop(k); del data[k]` - O(n − k)∗
* `data.remove(value)` - O(n)∗
* `data1.extend(data2);data1 += data2` - O(n2 )∗
* `data.reverse()` - O(n)
* `data.sort()` - O(n * log n)

### Python’s String Class

* Pattern matching - O(mn)
    `__contains__, find, index, count, replace, and split`
* Composing Strings
    * O(n^2)
    ```python
    letters = ''
    for c in document:
        if c.isalpha():
            letters += c
    ```
    * O(n)
    ```python
    temp = [ ]
    for c in document:
        if c.isalpha(): 
            temp.append(c)
    letters = ''.join(temp)
    ```
    
### Sorting a Sequence
#### The Insertion-Sort Algorithm
```python
def insertion_sort(A):
    for k in range(1, len(A)):
        cur = A[k]
        j=k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j-=1
        A[j] = cur    
```