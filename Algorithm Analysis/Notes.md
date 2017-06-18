## Experimental Studies

### Ways to measure algorithm execution time
* using the `time` function of the `time` module (wall-clock time)
```python
    from time import time
    start_time = time()
    # run algorithm
    end_time = time()
    elapsed = end_time - start_time
```
* using the `clock` function of the `time` module
    * measures how much time CPU spent on executing a program
* `timeit` module
* Counting Primitive Operations

## Functions Used in The Analysis of Algorithms

* The Constant Function
    ```
    f(n) = c
    ```
* The Logarithm Function
    ```
    f(n) = log b (n)
    ```
* The Linear Function
    ```
    f(n) = n
    ```
* The N-Log-N Function
    ```
    f(n) = n log n
    ```
* The Quadratic Function
    ```
    f(n) = n^2
    ```
* The Cubic Function and Other Polynomials
    ```
    f(n) = n^3
    f(n) = a0 + a1*n + a2*n^2 + a3*n^3 +···+ad*n^d
    ```
    * d - degree of the polynomial
* The Exponential Function
    ```
    f(n) = b^n
    ```
    
## Asymptotic Analysis
* The “Big-Oh” Notation
    * Let f(n) and g(n) be functions mapping positive integers to positive real numbers. 
        We say that f(n) is O(g(n)) if there is a real constant c > 0 and an integer constant n0 ≥ 1 such that
        ```
        f(n) ≤ cg(n), for n ≥ n0
        ```
        `f(n) is big-Oh of g(n).`
* Big-Omega
    * Let f(n) and g(n) be functions mapping positive integers to positive real numbers.
         We say that f(n) is Ω(g(n)), if g(n) is O(f(n)), that is, 
         there is a real constant c > 0 and an integer constant n0 ≥ 1 such that
         ```
         f(n) ≥ cg(n), for n ≥ n0
         ```
         `f(n) is big-Omega of g(n)`
         
* Big-Theta        
    * We say that f(n) is Θ(g(n)), if f(n) is O(g(n)) and f(n) is Ω(g(n)), that is, 
        there are real constants c1> 0 and c2> 0, and an integer constant n0 ≥ 1 such that
        ```
          c1 * g(n) ≤ f(n) ≤ c2 * g(n)
        ```
        `f(n) is big-Theta of g(n)`
        
## Algorithm Analysis
```python
    def find_max(data):
        biggest = data[0] 
        for val in data:
            if val > biggest:
            biggest = val
        return biggest
```
* `len(data)` - O(1)
* `data[0]` - O(1) - lists are implemented as array-based sequences, 
    references to a list’s elements are stored in a consecutive block of memory
* `find_max` - O(n) 

##Prefix Averages
* Quadratic-Time Algorithm
    ```python
        def prefix_average1(S):
            n = len(S)
            A = [0] * n
            for j in range(n):
                total = 0
                for i in range(j + 1): 
                    total += S[i]
                A[j] = total / (j+1)
            return A
    ```
    * `n = len(S)` - O(1)
    * `A = [0] * n` - O(n)
    * `total = 0` - O(n)
    * `total += S[i]` - O(n^2)
    * `A[j] = total / (j+1)` - O(n)
     ```python
        def prefix_average2(S):
            n = len(S)
            A = [0] * n
            for j in range(n):
                A[j] = sum(S[0:j+1]) / (j + 1)
            return A
    ```
    * `A[j] = sum(S[0:j+1]) / (j + 1)` - O(n^2)
    
* Linear-Time Algorithm
    ```python
        def prefix_average3(S):
            n = len(S)
            A = [0] * n
            total = 0
            for j in range(n):
                total += S[j]
                A[j] = total / (j+1)
            return A
    ```
    * `total += S[j]` - O(n)
    * `A[j] = total / (j+1)` - O(n)

## Three-Way Set Disjointness
* O(n^3)
    ```python
        def disjoint1(A, B, C):
            for a in A:
                for b in B: 
                    for c in C:
                        if a == b == c: 
                            return False
            return False
    ```
* O(n^2)
    ```python
        def disjoint1(A, B, C):
            for a in A:
                for b in B: 
                    if a == b:
                        for c in C:
                            if a == c: 
                                return False
            return False
    ```    

## Element Uniqueness
* O(n^2)
```python
    def unique1(S):
        for j in range(len(S)):
            for k in range(j+1, len(S)): 
                if S[j] == S[k]:
                    return False
        return False
```
* O(n log n) 
```python
    def unique2(S):
        temp = sorted(S) #O(nlogn)
        for j in range(1, len(temp)):
            if S[j−1] == S[j]: 
                return False
        return False
```