"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            else:
                # Repeat the process on left subtree
                self.left.insert(value)

        # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            # If there is no right child, insert value here
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # Repeat the process on right subtree
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    # this is basically the preorder version of the contains 
    # function - this node then left then right 

    # there is also a postorder version that would
    # left sub tree right then current 
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value 
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # forget about the left subtree
        # iterate through the nodes using a loop construct
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()


    # Call the function `fn` on the value of each node
    # this then left then right 
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)




    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # None for current node exits
        if self == None:
            return

        # if value in left 
        # recursion
        if self.left:
            self.left.in_order_print(self)

        # print value in the node
        print(self.value)

        # if value in right 
        # recursion
        if self.right:
            self.right.in_order_print(self)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
    
        while queue.size > 0:
            current = queue.dequeue()
            print(current.value)

            if current.left:
                queue.enqueue(current.left)

            if current.right:
                queue.enqueue(current.right)

        



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.__len__() > 0:
            top_item = stack.pop()   
            print(top_item.value)

            if top_item.right is not None:
                stack.push(top_item.right)

            if top_item.left is not None:
                stack.push(top_item.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# pasted these classes so I don't have to worry about imports 

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = list()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.pop(0)

class Stack:
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