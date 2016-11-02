# A similar, but different kind of control is done using `while`
# This is a simple test against a given condition, which then
# executes a block of code. If the condition is still true, the
# block will repeat, and until it becomes false.

answer = input("You're driving. Go left or right?")
while answer == "right":
    print("You turn right.")
    answer = input("You're driving. Go left or right?")

# which could be combined with an if/elif/else
if answer == "left":
    print("You turned left, good job!")
    print("I guess that's it.")
elif answer == "i don't know what to do!":
    print("You should turn right!")
elif answer == '':
    while answer == '':
        answer = input("I require an answer.")
elif answer == "stop":
    print("You screech to a stop")
else:
    print(answer)
    print(type(answer))
    print("ok.")

print("Thanks for playing!")
