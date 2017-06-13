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