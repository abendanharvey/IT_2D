# Assessment 3.2: Linear Data Structure
# Name: John Harvey A. Abendan
# Data Structure: Queue (FIFO)

from collections import deque

queue = deque()

print("ADDING LETTERS TO QUEUE")

# Enqueue each letter
for letter in "ABENDAN":
    queue.append(letter)

print("Initial Queue:", list(queue))

print("\nREMOVING LETTERS FROM QUEUE")

# Dequeue the first letter until the queue is empty
while len(queue) > 0:
    removed = queue.popleft()
    print("Dequeue", removed, ":", list(queue))

print("\nQueue is now empty!")
