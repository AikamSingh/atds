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
        found = False
        while current != None and not found:
            if current.get_data() == n:
                found = True
            else:
                current = current.get_next()
        return found




def main():
    n = Node(3)
    n2 = Node(2)
    n.set_next(n2)
    print(n)



if __name__ == '__main__':
    main()