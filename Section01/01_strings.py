# Strings

# Can be declared

myString = 'Oh, hello.'

# Can access elements via index

myString[4]
# >> out: 'h'

# Can get a range of elements using ':'

myString[4:8]
# >> out: 'hell'

# Can use ':' to get all the elements before index

myString[:4]
# >> out: 'Oh, '

# Can use ':' to get all the elements after an index

myString[6:]
# >> out: 'llo.'

# If we use ':' with no indices, we get back a copy of the string

myString[:]
# >> out: 'Oh, hello.'

# We can get the length with `len(string)`

len(myString)
# >> out: 10

# Get the elements in reverse order with `string[-n]`

myString[-1]
# >> out: '.'

# Can use a step operator as a 3rd argument

myString[::2]
# >> out: 'O,hlo'

# Step-argument `String[::n]` can be used to reverse output order

myString[::-1]
# >> out: '.olleh ,hO'
