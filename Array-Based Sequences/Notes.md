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

##Amortized Analysis of Dynamic Arrays