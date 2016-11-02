# We can bring input into the program with `input()` built-in

text = input('Type a phrase...')
### waits for user to press 'enter'
### value is then bound to variable
print(text)
### >> I typed a thing

# `input()` will always return a String, so we'll have to cast
# whenever dealing with numbers.

numbers = int(input("Choose a number between 1 and 100."))
print(numbers)
# >> 42
