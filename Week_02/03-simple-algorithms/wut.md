## Strings

#### Slicing `string[::]`

`[start:stop:step]`

- `start` : the index where the slicing function begins
- `stop`  : the index where the slicing function ends
- `step`  : special argument, can indicate string reversal (when `-1`), or how many indices to skip for every element returned by the slicing function

```python
s = "abcdefgh"

s[::-1]     # -> "hgfedcba"
s[3:6]      # -> "def"
s[-1]       # -> "h"
```

---

Strings are _immutable_ - they cannot be modified.
```python
s = "hello"
s[0] = "y"              # -> error
s = 'y' + s[1:len(s)]   # -> allowed, but s is a new object
```

#### Strings are iterable

Two ways of writing the same function:
```python
s = "abcdefgh"
for index in range(len(s)):
  if s[index] == "i" or s[index] == "u":
    print("The is an i or u")

# Or, use the iterable property of `s`

for char in s:
  if char == "i" or char == "u":
    print("There is an i or u")

```
