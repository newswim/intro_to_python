Iterative Algorithms

Bindings = Variables


#### Reserved words

- [Table of Python Keywords](https://learnpythonthehardway.org/book/ex37.html)
- [Table of Python Built-In Functions](https://docs.python.org/3/library/functions.html)

### Notes on built-in functions

- [Range is actually an immutable data type](https://docs.python.org/3/library/functions.html#func-range)

## Cast types with built-in function calls

```py
x = 4
y = 'hello'
z = 1.0
float(x)
# >> 4.0
str(x)
# >> '4'
int(z)
# >> 1
```


## `for` vs. `while` loops

| For                                              | While                                                                            |
|:-------------------------------------------------|:---------------------------------------------------------------------------------|
| _know_ number of iterations                      | _unbounded_ number of iterations                                                 |
| can _end early_ via `break`                      | can _end early_ via `break                                                       |
| uses a _counter_                                 | can use a _counter but must initialize_ before loop and increment it inside loop |
| _can rewrite_ a `for` loops using a `while` loop | _may not be able to rewrite_ a `while` loop using a `for` loop                   |
