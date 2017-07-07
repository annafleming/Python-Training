## The Basics Of Binary
* Convert from binary to base 10
`base_10_100 = int("100", 2)`
* Add 2 binaries
`bin(int("10", 2) + int("100", 2)))[2:]` 
* Get the integer for an ASCII character.
`ord('a')`
* Convert to binary, hexadecimal
`bin(10)`
`hex(10)`
* Encode the string into bytes(similar to a string, except that it contains encoded bytes values)
`.encode()`
* Bytes datatype
```python
hulk_bytes = b"Bruce Banner"
hulk_bytes.replace(b"Banner", b"")
hulk_str = hulk_bytes.decode("utf-8")
```
## Count The Tokens
```python
from collections import Counter
fruits = ["apple", "apple", "banana", "orange", "pear", "orange", "apple", "grape"]
fruit_count = Counter(fruits)
fruit_count.most_common(2)
```