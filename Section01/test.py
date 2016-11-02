print("Python has a for...in expression used on iterable collections")

for i in range(5):  # range(n) is a built-in collection generator
    print(i)

print("If we want to cease iteration at a specific point, we can use 'break'")

myVar = 0

for y in range(2, 10):
    print(y)
    myVar += y
    if y == 6:
        print(myVar)
        break

print('test')
print(myVar)
