# Assessment 3.2: Linear Data Structure
# Name: John Harvey A. Abendan
# Data Structure: Array

letters = []

# Add each letter of my last name
print("ADDING LETTERS TO ARRAY")

for letter in "ABENDAN":
    letters.append(letter)

print("Initial Array:", letters)

# Remove the last letter one by one
print("\nREMOVING LETTERS FROM ARRAY")

while len(letters) > 0:
    removed = letters.pop()
    print("Remove", removed, ":", letters)

print("\nArray is now empty!")
