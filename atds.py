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
        self.val = val
        self.left = None
        self.right = None
    
    def get_root_val(self):
        return self.val
    
    def set_root_val(self, v):
        self.val = v

    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right
    
    def insert_left(self, new_left_val):
        new_subtree = BinaryTree(new_left_val)
        new_subtree.left = self.left
        self.left = new_subtree
        
    
    def insert_right(self, new_right_val):
        new_subtree = BinaryTree(new_right_val)
        new_subtree.right = self.right
        self.right = new_subtree
    
    def __repr__(self):
        return "BinaryTree[key=" + str(self.val) + ",left_child=" + str(self.left) + ",right_child=" + str(self.right) + "]"

class BinaryHeap(object):
    """Describes a BinaryHeap tree"""
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
    
    def percolate_up(self,i):
        while i // 2 > 0:
            print(i)
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
                i = i // 2
            else:
                return
    
    def percolate_down(self,i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc
    
    def insert(self,k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.percolate_up(self.current_size)
    
    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def find_min(self):
        return self.heap_list[1]
    
    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.percolate_down(1)
        return ret_val
    
    def is_empty(self):
        if self.current_size == 0:
            return True
        else:
            return False
    
    def size(self):
        return self.current_size
    
    def build_heap(self, value_list):
        i = len(value_list) // 2
        self.current_size = len(value_list)
        self.heap_list = [0] + value_list[:]
        while (i > 0):
            self.percolate_down(i)
            i = i - 1

    def __repr__(self):
        return "BinaryHeap" + str(self.heap_list)

class HashTable():
    """Describes a hash table that will store key-value pairs.
    One way to do this would be to create a single array of dictionary-style
    objects. Another strategy--simultaneously simpler and more cumbersome--
    is to maintain a pair of parallel arrays. One array--slots--keeps track
    of the keys, while a second array--data--stores the value associated with
    each key.
    
    At the beginning, the parallel arrays for a hash table of size 7 look like 
    this:
    
        slots = [ None, None, None, None, None, None, None ]
    
        data =  [ None, None, None, None, None, None, None ]
        
    Calling the .put(key, value) method will update the slots and data in 
    those arrays:
    
        .put(8, "Adam")
        
    Updated hash table (based on slot 8 % 7 = 1)
     
        slots = [ None,    8  , None, None, None, None, None ]
    
        data =  [ None, "Adam", None, None, None, None, None ]
    
    """
    
    
###############################

    def __init__(self, m):
        """Creates an empty hash table of the size m
        """
        self.size = m                       # remember, prime numbers are better
        self.slots = [None] * self.size     # a list of None keys
        self.data = [None] * self.size      # a list of None values

###############################

    def hash_function(self, key, size):
        """This helper method returns the value of the hash function, based on 
        the key and the size of the table.
        """
        return key % size

###############################

    def put(self, key, value):
        """Places a key-value pair in the hash table, or replaces
        the current value if the key already exists in the table.
        """
        hash_value = self.hash_function(key, self.size)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                next_slot = self.rehash(hash_value, self.size)
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, self.size)
                
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = value
                else:
                    self.data[next_slot] = value

###############################

    def get(self, key):
        """Tries to find a key-value pair in the hash table, or returns
        None if no key is found.
        """
        start_slot = self.hash_function(key, self.size)

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, self.size)
                if position == start_slot:
                    stop = True
        return data
        
###############################

    def rehash(self, old_hash, size):
        """Returns a new hash value based on the old hash value.
        """
        return (old_hash + 1) % size

###############################

    def __repr__(self):
        """Returns a string representation of the hash table, displayed 
        as two arrays.
        """
        return "Keys:   " + str(self.slots) + "\n" + "Values: " + str(self.data)
    
    class Vertex(object):
    """Describes a vertex object in terms of a "key" and a
    dictionary that indicates edges to neighboring vertices with
    a specified weight.
    """
    
    def __init__(self, key):
        """Constructs a vertex with a key value and an empty dictionary 
        in which we'll store other vertices to which this vertex is
        connected.
        """
        self.id = key
        self.connected_to = {}   # empty dictionary for neighboring vertices
        self.color = 'white'
        self.distance = 0
        self.predecessor = None
        self.discovery_time = 0     # discovery time
        self.finish_time = 0        # finish time  
    
    def add_neighbor(self, neighbor_vertex, weight=0):
        """Adds a reference to a neighboring Vertex object to the
        dictionary, to which this vertex is connected by an edge. 
        If a weight is not indicated, default weight is 0.
        """
        self.connected_to[neighbor_vertex] = weight
    
    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_distance(self, distance):
        self.distance = distance
    
    def get_distance(self):
        return self.distance
    
    def set_pred(self, predecessor):
        self.predecessor = predecessor
    
    def get_pred(self):
        return self.predecessor
    
    def set_discovery(self, discovery_time):
        self.discovery_time = discovery_time
    
    def get_discovery(self):
        return self.discovery_time
    
    def set_finish(self, finish_time):
        self.finish_time = finish_time
    
    def get_finish(self):
        return self.finish_time
    
    def __repr__(self):
        """Returns a representation of the vertex and its neighbors,
        suitable for printing. Check out the example of 'list
        comprehension' here!
        """
        return 'Vertex[id=' + str(self.id) \
                + ',color=' + self.color \
                + ',dist=' + str(self.distance) \
                + ',pred=' + str(self.predecessor) \
                + ',disc=' + str(self.discovery_time) \
                + ',fin=' + str(self.finish_time) \
              + '] connected_to: ' + str([x.id for x in self.connected_to]) 
    
    def get_connections(self):
        """Returns the keys of the vertices we're connected to
        """
        return self.connected_to.keys()
    
    def get_id(self):
        """Returns the id ("key") for this vertex
        """
        return self.id
    
    def get_weight(self, neighbor_vertex):
        """Returns the weight of an edge connecting this vertex 
        with another.
        """
        return self.connected_to[neighbor_vertex]

class Graph(object):
    """Describes the Graph class, which is primarily a dictionary
    mapping vertex names to Vertex objects, along with a few methods
    that can be used to manipulate them.
    """
    def __init__(self):
        """Initializes an empty dictionary of Vertex objects
        """
        self.graph = {}

    def add_vertex(self, key):
        """Creates a new "key-value" dictionary entry with the string "key"
        key as the dictionary key, and the Vertex object itself as the value.
        Returns the new vertex as a result.
        """
        new_vertex = Vertex(key)
        self.graph[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        """Looks for the key in the dictionary of Vertex objects, and
        returns the Vertex if found. Otherwise, returns None.
        """
        if key in self.graph.keys():
            return self.graph[key]
        else:
            return None

    def __contains__(self, key):
        """This 'dunder' expression is written so we can use Python's "in"
        operation: If the parameter 'key' is in the dictionary of vertices,
        the value of "key in my_graph" will be True, otherwise False.
        """
        return key in self.graph.keys()

    def add_edge(self, from_key, to_key, weight=0):
        """Adds an edge connecting two vertices (specified by key
        parameters) by modifying those vertex objects. Note that
        the weight can be specified as well, but if one isn't
        specified, the value of weight will be the default value
        of 0.
        """
        # if the from_key doesn't yet have a vertex, create it
        if from_key not in self.get_vertices():
            self.add_vertex(from_key)
        # if the to_key doesn't yet have a vertex, create it
        if to_key not in self.get_vertices():
            self.add_vertex(to_key)
        # now we can create the edge between the two
        self.get_vertex(from_key).add_neighbor(self.get_vertex(to_key), weight)

    def get_vertices(self):
        """Returns a list of the Graph's Vertex keys"""
        return self.graph.keys()

    def __iter__(self):
        """Another 'dunder' expression that allows us to iterate through
        the list of vertices.
        Example use:
        for vertex in graph:  # Python understands this now!
            print(vertex)
        """
        return iter(self.graph.values())



def main():
    ul = UnorderedList()
    ul.add(3)
    ul.add(4)
    print(ul.search(3))
    print(ul.search(2))
    print(ul)



if __name__ == '__main__':
    main()
