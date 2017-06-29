## The Factorial Function
```python
    def factorial(n): 
        if n == 0:
            return 1 
        else:
            return n * factorial(n−1)
```

## Binary Search
* sequential search runs in O(n) time, binary search runs in O(logn) time

## Python’s os Module
* os.path.getsize(path)
* os.path.isdir(path)
* os.listdir(path)
* os.path.join(path, filename)

## Maximum Recursive Depth in Python
* typical default value is `1000`
```python
import sys
old = sys.getrecursionlimit() 
sys.setrecursionlimit(1000000)
```

## Examples of Recursion
###  Linear recursion
recursive call starts at most one other
* Summing the Elements of a Sequence Recursively - `O(n)`
```python
def linear_sum(S, n):
    if n == 0:
        return 0 
    else:
        return linear_sum(S, n-1) + S[n-1]
```
* Reversing a Sequence with Recursion - `O(n)`
```python
def reverse(S, start, stop):
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start] 
        reverse(S, start + 1, stop - 1)
```

### Binary Recursion
function makes two recursive calls
* summing the n elements of a sequence
```python
def binary_sum(S, start, stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, start, mid)
```

### Multiple Recursion
function may make more than two recursive calls
* analyzing the disk space usage of a file system

## Designing Recursive Algorithms
* `Test for base cases` - We begin by testing for a set of base cases (there should be at least one). These base cases should be defined so that every possible chain of recursive calls will eventually reach a base case, and the handling of each base case should not use recursion.
* `Recur` - If not a base case, we perform one or more recursive calls.

## Eliminating Tail Recursion
_Tail recursion_ - a recursion is a tail recursion if any recursive call that is made from one context is the very last operation in that context, with the return value of the recursive call (if any) immediately returned by the enclosing recursion