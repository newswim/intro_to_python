## Functions!

Functions give us a means of describing **Abstraction** and **Decomposition**.

Python functions should usually take the following structure:

```python

def functionName (params):
  '''
  Docstring
  params: the inputs the function, and their types
  return: a description of the return value and its type
  '''
  return (params)

```


### Variable Scope

Each function has its own variable scope. It can inherit from the `Global` scope, but
it cannot modify variables within the Global scope, unlike JavaScript.

### Default Parameters

Similar to JS:

```python
def printName(firstName, lastName, reverse = False):
  if reverse:
    print(lastName + ', ' + firstName)
  else:
    print(firstName, lastName)
```

In this function, the parameter `reverse` has a default value of `False`.

## Specifications

Usually consisting of two parts:

- **Assumptions**: those things which the implementor is expecting to hold true
- **Guarantees**: what the function will do, depending on the Assumptions being true

We achieve this in Python by using a `Docstring`

```python
c = 12
def is_even(i):
  '''
  Input: i, a positive integer
  Returns True if `i` is even, otherwise returns False
  '''
  return i % 2 == 0
```

## Recursion
