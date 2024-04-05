#!/usr/bin/env python3

"""
atds.py
The module containing all the data structures used in the Advanced Topics course
"""

__author__ = 'Aikam Singh'
__version__ = '2024-02-13'

class Stack(object):
    """this class defines a stack data structure"""
    def __init__(self):
        self.s = []

    def push(self, item):
        """adds an object to the top of the stack"""
        self.s.append(item)

    def pop(self):
        """removes the top item from the stack"""
        if self.is_empty():
            return None
        else:
            return self.s.pop()

    def peek(self):
        """returns the top object from the stack"""
        if self.is_empty():
            return None
        else:
            return self.s[-1]

    def size(self):
        """returns the size of the stack"""
        return len(self.s)

    def is_empty(self):
        """returns true if the stack is empty"""
        return len(self.s) == 0

class Queue(object):
    """this class defines a queue data structure"""
    def __init__(self):
        self.q = []
    
    def enqueue(self, i):
        self.q.append(i)
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.q.pop(0)
    
    def size(self):
        """returns the size of the stack"""
        return len(self.q) 
    
    def peek(self):
        """returns the top object from the stack"""
        if self.is_empty():
            return None
        else:
            return self.s[0]
    
    def is_empty(self):
        """returns true if the stack is empty"""
        return len(self.q) == 0

class Deque(object):
    """deque data structure"""
    def __init__(self):
        self.d = []
    
    def add_front(self, item):
        self.d.insert(0, item)
    
    def add_rear(self, item):
        self.d.append(item)
    
    def remove_front(self):
        return self.d.pop(0)
    
    def remove_rear(self):
        return self.d.pop()
    
    def size(self):
        """returns the size of the stack"""
        return len(self.d)
    
    def is_empty(self):
        """returns true if the stack is empty"""
        return len(self.d) == 0

class Node(object):
    """Implements a node object, to be used in an unordered list"""
    def __init__(self, data):
        self.d = data
        self.n = None
    
    def set_data(self, data):
        self.d = data
    
    def get_data(self):
        return self.d
    
    def set_next(self, next):
        self.n = next
    
    def get_next(self):
        return self.n

    def __repr__(self):
        return "Node[data=" + str(self.d) + ",next=" + str(self.n) + "]"

class UnorderedList(object):
    """Defines an unordered (unsorted) using a series of Nodes"""

    def __init__(self):
        self.head = None
    
    def add(self, n):
        """creates a new node based on the data, and adds it to the beginning of the list"""
        temp_node = Node(n)
        temp_node.set_next(self.head) 
        self.head = temp_node #changes head to reference the node, instead of the None value
    
    def length(self):
        """traverses the entire length of the list and returns the number of Nodes there are in the list"""
        node_count = 0
        current = self.head
        while current != None:
            current = current.get_next()
            node_count += 1
        return node_count
    
    def search(self, n):
        """Traverses through the list to determine if the indicated data 
        is present.
        """
        current = self.head
        while current != None:
            if current.get_data() == n:
                return True #returns true if the data is present
            else:
                current = current.get_next()
        return False #returns false if the data is not present
    
    def remove(self, data):
        """Removes all occurrences of the specified data from the list."""
        previous = None
        current = self.head
        
        while current is not None:
            if current.get_data() == data:
                if previous is None:
                    self.head = current.get_next()
                    current = self.head
                else:
                    previous.set_next(current.get_next())
                    current = current.get_next()
            else:
                previous = current
                current = current.get_next()
        
    def is_empty(self):
        """returns True if the list if empty"""
        return self.head == None
    
    def append(self, item):
        """appends a new item to the end of the linked list"""
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        temp_node = Node(item)
        current.set_next(temp_node)
    
    def index(self, item):
        """returns the position of the item in the list (and assumes it is in the list)"""
        current = self.head
        index = 0
        while current != None:
            if current.get_data() == item:
                return index
            else:
                current = current.get_next()
                index += 1
    
    def insert(self, pos, item):
        """adds a new item to the list at the specified position. This assumes that the item is not already on the list and that the position exists."""
        if pos == 0:
            self.add(item)
        else:
            current = self.head
            previous = None
            current_pos = 0
            while current_pos < pos and current != None:
                previous = current
                current = current.get_next()
                current_pos += 1
            new_node = Node(item)
            previous.set_next(new_node)
            new_node.set_next(current)
    
    def pop(self, pos=None):
        """removes the last item from the list and returns it.
        If position is specified, it removes and returns item at that position."""
        if pos is None:
            current = self.head
            previous = None
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            if previous is None:
                self.head = None
            else:
                previous.set_next(None)
            return current.get_data()
        else:
            if pos == 0:
                item = self.head.get_data()
                self.head = self.head.get_next()
                return item
            else:
                current = self.head
                previous = None
                current_pos = 0
                while current_pos < pos and current != None:
                    previous = current
                    current = current.get_next()
                    current_pos += 1
                if current is None:
                    return None
                else:
                    previous.set_next(current.get_next())
                    return current.get_data()

    def __repr__(self):
        """Creates a representation of the list suitable for 
        printing, debugging.
        """ 
        return_value = "UnorderedList["
        next_node = self.head
        while next_node != None:
            return_value += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        return_value = return_value + "]"
        return return_value
        
class ULStack(object):
    """this class describes a stack made with the UnorderedList class"""
    def __init__(self):
        self.items = UnorderedList()
    
    def push(self, item):
        """adds an item to the beginning of the stack"""
        self.items.add(item)
    
    def pop(self):
        """removes and returns the item at position 0 from the stack"""
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        """returns the value of the first item in the stack"""
        if self.is_empty():
            return None
        return self.items.head.get_data()

    def size(self):
        """returns the size of the stack"""
        return self.items.length()

    def is_empty(self):
        """returns true if the stack is empty, false if it has items"""
        return self.items.is_empty()

class HashTable(object):
    """Describes a hash table based on two lists, `slots` and `values`,
    and describes putting and getting values onto that table.
    Hash function is the mod (%) function, and collisions are handled
    using linear probing.
    """
    def __init__(self, size):
        """Create empty lists for the Map
        """
        self.keys = size * [None]
        self.data = size * [None]
        self.size = size

    def put(self, key, value):
        """Creates an entry in the hash table
        """
        hash_value = key % self.size        # index for key & value
        while self.keys[hash_value] != None and self.keys[hash_value] != key:
            hash_value += 1
        # We're at a position where we can place the value
        if self.keys[hash_value] == key:
            self.data[hash_value] = value
        else:
            self.keys[hash_value] = key
            self.data[hash_value] = value

    def get(self, key):
        hash_value = key % self.size
        while self.keys[hash_value] != None and self.keys[hash_value] != key:
            hash_value += 1
        if self.keys[hash_value] == key:
            return self.data[hash_value]
        else:
            return None

    def __str__(self):
        return "Keys:   " + str(self.keys) + "\n" + \
               "Values: " + str(self.data)

class BinaryTree(object):
    """Describes a BinaryTree object which contains nodes that point to two children."""

    def __init__(self, val):
        """initiates a binary tree with a root value and no children"""
        self.val = val
        self.left = None
        self.right = None
    
    def get_root_val(self):
        """returns the root value"""
        return self.val
    
    def set_root_val(self, v):
        """sets the root value"""
        self.val = v

    def get_left_child(self):
        """returns the left child"""
        return self.left
    
    def get_right_child(self):
        """returns the right child"""
        return self.right
    
    def insert_left(self, new_left_val):
        """inserts a new left value and shifts the already existing left value. ex. if we had a --> b and we inserted c, then it would be a --> c --> b."""
        new_subtree = BinaryTree(new_left_val)
        new_subtree.left = self.left
        self.left = new_subtree
        
    
    def insert_right(self, new_right_val):
        """inserts a new right value and shifts the already existing right value. ex. if we had a --> b and we inserted c, then it would be a --> c --> b."""
        new_subtree = BinaryTree(new_right_val)
        new_subtree.right = self.right
        self.right = new_subtree
    
    def __repr__(self):
        return "BinaryTree[key=" + str(self.val) + ",left_child=" + str(self.left) + ",right_child=" + str(self.right) + "]"


def main():
    ul = UnorderedList()
    ul.add(3)
    ul.add(4)
    print(ul.search(3))
    print(ul.search(2))
    print(ul)



if __name__ == '__main__':
    main()
