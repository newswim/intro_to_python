### Compute the square root of a number

- The square root of a number `x` is `y` such that `y * y = x`.

A 'recipe', or algorithm, or imperative construction of knowledge may resemble the following:

1) Start with a _guess_, `g`
2) If `g * g` is *close enough* to `x`, stop and say `g` is the answer
3) Otherwise, make a new guess by averaging `g` and `x/g`
4) Using the new guess, *repeat* the process until it's _close enough_.

> `x = 16`

| `g`    | `g * g` | `x / g` | `(g + x/g) / 2` |
|:-------|:--------|:--------|:----------------|
| 3      | 9       | 5.333   | 4.1667          |
| 4.1667 | 17.36   | 3.837   | 4.0035          |
| 4.0035 | 16.0277 | 3.997   | 4.000002        |

We might then say that 4 is _close enough_.

---

Note: this method for finding the square root of a number is attributed to Heron of Alexandria, dating back to 2nd century BC.

#### What is an algorithm?

1) a sequence of simple *steps*
2) *flow of control* process that specifies when each step is executed
3) a means to determining *when to stop*

##### Steps 1+2+3 = an `algorithm`!

### Store Program Computer

- Sequence of *instructions stored* inside computer
  - built from predefined set of primitive instructions
    1) arithmetic and logic
    2) simple tests
    3) moving data
- Special program (interpreter) *executes each instruction in order*
  - use tests to change flow of control through sequence
  - stop when done

## Basic Primitives

Turing showed you can *computer anything* using 6 primitives. Modern programming languages have more convenient set of primitives and can *_abstract_* methods *to create new primitives*. Turing showed that anything computable in one language is computable in any other programming language.

- Following these rules, a programming language is said to be *Turing Complete*.

## Aspects of Language

Syntax and Semantics

- *Primitive Constructs*
  - English: words
  - programming languages: numbers, strings, simple operators (`float`, `bool`, `int`, `NoneType`, `==`, `+`, `%`)
- Syntax
  - English:
    - "cat dog boy" ---> not syntactically valid
    - "cat hugs boy" --> is syntactically valid
  - programming language:
    - "hi"5 ---> no
    - 3.2 * 5 -> yes

#### Static Semantics

Statements in which syntactically valid strings have meaning.

- English: "I are hungry"
  - Syntactically valid
  - Renders static semantic error
- programming language:
  - 3.2 * 5
    - valid both syntactically and semantically
  - 3 + "hi"
    - valid syntactically
    - static semantic error

Semantics is the meaning associated with a syntactically correct string of symbols with no semantic errors.

- English: can have many meanings
  - "Flying planes can be dangerous"
  - "This reading lamp hasn't uttered a word since I bought it"
programming languages: have only one meaning butmay not be what the programmer intended.

## Where do things go wrong?

1) *syntactic errors*
  - common, easily caught
2) *static semantic errors*
  - some languages check for these before running program
  - can cause unpredictable behavior
3) no semantic errors but *different meaning than what programmer intended*
  - program crashes, stops running
  - program runs forever
  - program gives an answer but different than expected

---

## Python Programs

A *program* is a square of definitions and commands
  - definitions get _evaluated_
  - commands get _executed_ by the Python interpreter in a shell

*Commands* or _statements_ instruct the interpreter to do something

They can be typed directly into a *shell*, or store in a file that is read into the shell and evaluated.

### Objects

Programs manipulate *data objects*. Objects have a *type* that defines the kinds of things the program can do with them.

Objects are:
  - scalar (cannot be subdivided)
  - non-scalar (have internal structure than can be accessed)

#### Scalar Objects

- `int` - represents *integers*, ex. 5
- `float` - represent *real numbers*, ex. 3.27
- `bool` - represent *Boolean* values, `True` and `False`
- `NoneType` - is *special* and has one value, `None`

We can use `type()` to see the type of an object.
```python
type(5)    # >> int
type(3.0)  # >> float
```
