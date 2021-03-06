# Python’s Built-In Classes

* bool
* int
   - `int( 7f , 16)` evaluates to the integer 127
* float 
   - 6.022e23 represents the mathematical value 6.022 × 1023 
* list - mutable sequence of objects []
   - `list( 'hello' )` produces a list of individual characters
* tuple - immutable sequence of objects ()
   - `(17,)` is a one-element tuple
* str - character string
   - supports using the delimiter ''' or """ to begin and end a string literal
* set - unordered set of distinct objects {}
   - based on _hashtable_
   - does not maintain order
   - only instances of immutable types can be added to a set
* frozenset - immutable form of _set_ class
   - enables to have a set of frozensets
* dict - associative mapping (aka dictionary)

## Equality Operators

* __is / is not__ - Identity operators (True if refer to the same object)
* __== / !=__ - Equivalent / Not Equivalent

## Sequence Operators
* s[j], s[start:stop], s[start:stop:step]
* s[start:stop] 
* s[start:stop:step]
* s+t, k*s 
* `val in s` (can also be used for Strings)

## Iterators and Generators
* iterator
     * i = iter(data); next(i)
* generator
    ``` python
    def factors(n):
        for k in range(1,n+1):
            if n % k == 0: 
                yield k
    ```
    
    
## Additional Python Conveniences
    
* Conditional Expressions
    ``` python
        param = n if n >= 0 else −n
    ```
    
* List comprehensions
    * list comprehension `[ k k for k in range(1, n+1) ]`
    * set comprehension `{ k k for k in range(1, n+1) }`
    * generator comprehension `( k k for k in range(1, n+1) )`
    * dictionary comprehension `{ k : k k for k in range(1, n+1) }`

* Packing
    * `data = 2, 4, 6, 8` - results in tuple `(2, 4, 6, 8)`

* Unpacking
    * `a, b, c, d = range(7, 11)`

* Simultaneous Assignments
    * `x, y, z = 6, 2, 5`
    * Swapping the values `j, k = k, j`

