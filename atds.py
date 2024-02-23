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

