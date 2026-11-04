# Assessment 3.2: Linear Data Structure
# Name: John Harvey A. Abendan
# Data Structure: Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

    def display(self):
        current = self.head
        elements = []

        while current:
            elements.append(current.data)
            current = current.next

        return elements

    def delete_first(self):
        if self.head is not None:
            removed = self.head.data
            self.head = self.head.next
            return removed


# Create an empty linked list
my_list = LinkedList()

print("ADDING LETTERS TO LINKED LIST")

for letter in "ABENDAN":
    my_list.insert(letter)

print("Initial List:", my_list.display())

print("\nREMOVING LETTERS FROM LINKED LIST")

while my_list.head is not None:
    removed = my_list.delete_first()
    print("Remove", removed, ":", my_list.display())

print("\nLinked List is now empty!")
