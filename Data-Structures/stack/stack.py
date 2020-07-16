print("stack py loaded")
from singly_linked_list.singly_linked_list import Node, LinkedList

"""
Stacks
Should have the methods: 
push, 
pop, and 
len.


A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class LucidStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

s = LucidStack()
s.push("A")
s.push("B")
print(s.get_stack())
s.push("C")
s.pop()
s.push("D")
print(s.get_stack())





class LinkedListStack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    # len returns the number of elements in the stack.
    def __len__(self):
        return self.size

    # push adds an item to the top of the stack.
    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    # pop removes and returns the element at the top of the stack
    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_tail()


class ListStack:
    def __init__(self):
        self.size = 0
        self.storage = list()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.pop()

