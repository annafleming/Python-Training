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