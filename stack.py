# Assessment 3.2: Linear Data Structure
# Name: John Harvey A. Abendan
# Data Structure: Stack (LIFO)

stack = []

print("ADDING LETTERS TO STACK")

# Push each letter into the stack
for letter in "ABENDAN":
    stack.append(letter)

print("Initial Stack:", stack)

print("\nREMOVING LETTERS FROM STACK")

# Pop the top letter until the stack is empty
while len(stack) > 0:
    removed = stack.pop()
    print("Pop", removed, ":", stack)

print("\nStack is now empty!")
