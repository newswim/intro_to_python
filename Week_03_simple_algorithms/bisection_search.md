```python
x = 25
epsilon = 0.01
numGuess = 0
low = 1.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
  print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
  numGuesses += 1
  if ans**2 < x:
      low = ans
  else:
      high = ans
  ans = (high + low) / 2.0

print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))
```

A really powerful way to cut down the number of computational steps needed to find and answer. In our example of this idea applied to _finding the square root_, the number of guesses required decreased from ~30k to just 14+-1.

We can even greatly increase the accuracy of our epsilon value and not suffer much in the way of penalties for computational time. For example, I've increased the number of zeroes to `0.0000001` and when using an example x, the function only took about 32 steps to find a good answer.

## Bisection Search Convergence

After just 3 guesses, we can derive a constant to describe the number of computations which will need to occur in order to find our answer.

|              	| Search Space 	|
|--------------	|--------------	|
| first guess  	| N/2          	|
| second guess 	| N/4          	|
| gth guess    	| N/2**g       	|

So we can say that the guess converges on the order of log₂N.

Bisection search works when the value of function varies with monotonically with input.

code shown only works for positive cubes > 1 -- Why is that?

### Challenges

- Modify the code to work with negative cubes (hint: `abs()`)
- Modify to work with x's less than 1.

#### `X < 1`

- If `x < 1`, search space is 0 to `x` but cube root is greater than `x` and less than 1.
- Modify the code to choose the search space depending on the value of `x`.

## Final Notes

- Bisection Search should work well on problems with an `'ordering'` property.
- Bisection Search radically reduces computation time by intelligently generating guesses.
