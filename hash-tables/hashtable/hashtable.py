class LinkedList:
    """
    Reuse old code to create a linked list for the assignment
    """

    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        size = 0
        if current.next is None:
            return 1
        else:
            while current != None:
                size += 1
                current = current.next

            return size

    # looking for key
    def search(self, key):
        current = self.head

        # TODO is not None
        # TODO versus != None
        while current != None:
            if current.key == key:
                return current
            # iterate through it now
            current = current.next

        # if the key is not found return None
        # if not found the current will be none so return current

        # TODO see what the difference is
        # !!! return current !!! test this versus returning None
        return None

    # I did not follow Beejs example of insert head
    # implement insert tail and hope it doesn't ruin everything

    def insert_tail(self, key, value):
        # if not head condition
        if self.head == None:
            # create a node to be the head
            new_node = HashTableEntry(key, value)
            # set self.head to the new node
            self.head = new_node

        # if head exists condition
        else:
            # search for the key we need
            node = self.search(key)

            # if match is found
            # if node is not None Condition
            # TODO is not None
            # TODO versus != None
            if node != None:
                node.value = value

            # if the key does not reside in LinkedList condition
            else:
                # new node time
                new_node = HashTableEntry(key, value)

                # start iterating
                current.self = head

                # TODO is not None
                # TODO versus != None
                while current.next != None:
                    # iterate through it now
                    current = current.next
                # set next node
                current.next = new_node

    def delete(self, key):

        # iterate through starting at the head
        current = self.head

        # if next is none head is none
        if current.next is None:
            self.head = None

        # if the current is the key to delete
        # set head as the current next
        elif current.key == key:
            self.head = current.next

        # if exists next node and is not key
        else:

            # start iterating through
            while current.next != None:

                # if the next node's key is the passed in key
                if current.next.key == key:

                    # set the current next node to None
                    current.next = None

                # if current next key is not key we are deleting
                else:
                    current = current.next


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        # self.next = None Not needed until linked list day two

    def __repr__(self):
        return f"HashTableEntry({repr(self.key)}, {repr(self.key)})"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        if capacity < MIN_CAPACITY:
            capacity = MIN_CAPACITY
        self.storage = [None] * self.capacity
        self.item_counter = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.item_counter / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for letter in key:
            hash = ((hash << 5) + hash) + ord(letter)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
