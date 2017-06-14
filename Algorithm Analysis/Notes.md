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
