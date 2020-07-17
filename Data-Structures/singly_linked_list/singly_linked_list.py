print("singly linked list loaded")
class Node:
    """
    Data:
    Stores two pieces of data:
    1. The Value
    2. The Next Node

    Methods/Behavior/Operations:
    1. Get Value
    2. Set Value
    3. Get Next
    4. Set Next
    """
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this nodes next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    """
    Data:
    1. A reference to the head Node
    2. A reference to the tail Node

    Behavior/Methods:
    1. Add to tail
    2. Prepend (Add a new node and point that Node's next_node at the old Head; update Head pointer)
    3. Remove Head
    4. Remove Tail
    5. Contains?
    6. Get Maximum?
    """

    def __init__(self):
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None

    def add_to_tail(self, value):
        # wrap the input value in a node
        new_node = Node(value, None)
        # check if there is no head(i.e., the list is empty)
        if not self.head:
            # if the list is initially empty, set both the Head and the Tail to the new Node
            self.head = new_node
            self.tail = new_node
        # if we have a non-empty list, add the new node to the tail
        else:
            # set the current tail's reference to the new node
            self.tail.set_next(new_node)
            # set the list's tail reference to the new node
            self.tail = new_node

    def remove_head(self):
        # return None if there is no Head
        if not self.head:
            return None
        # if the head has no next, then we have a single element in our list
        if not self.head.get_next():
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            # return the value
            return head.get_value()
        # otherwise if we have more than one element in our list
        value = self.head.get_value()
        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        # return None if empty
        if not self.head:
            return None
        # if the head has no next, then we have a single element in our list
        if self.head is self.tail:
            value = self.tail
            # delete the list's tail reference
            self.tail = None
            # also make sure head reference doesn't refer to anything
            self.head = None
            # return the value
            return value.get_value()
        # otherwise if we have more than one element in our list
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        self.tail.next_node = None
        return value

    def contains(self, value):
        if not self.head:
            return False

        # get a reference to the node we are currently at; update as we traverse the list
        current = self.head
        #check to see if we're at a valid node
        while current:
            # return True if the current value we're at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value iterable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value