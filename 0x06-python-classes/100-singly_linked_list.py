#!/usr/bin/python3
"class Node that defines a node of a singly linked list by"


class Node:
    """Private instance attribute: data:
    property def data(self): to retrieve it
    property setter def data(self, value): to set it:
    data must be an integer, otherwise raise a TypeError
    exception with the message data must be an integer
    Private instance attribute: next_node:
    property def next_node(self): to retrieve it
    property setter def next_node(self, value): to set it:
    next_node can be None or must be a Node, otherwise raise
    a TypeError exception with the message
    next_node must be a Node object
    Instantiation with data and
    next_node: def __init__(self, data, next_node=None):
    And, write a class SinglyLinkedList
    that defines a singly linked list by:

    Private instance attribute: head (no setter or getter)
    Simple instantiation: def __init__(self):
    Should be printable:
    print the entire list in stdout
    one node number by line
    Public instance method: def sorted_insert(self, value):
    that inserts a new Node into the correct sorted position
    in the list (increasing order)
    You are not allowed to import any module
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    "defines a singly linked list"
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.head is None or self.head.data >= new.data:
            new.next_node = self.head
            self.head = new
        else:
            present = self.head
            while present.next_node is not None and \
                    present.next_node.data < new.data:
                present = present.next_node
            new.next_node = present.next_node
            present.next_node = new

    def __str__(self):
        values = []
        present = self.head
        while present is not None:
            values.append(str(present.data))
            present = present.next_node
        return "\n".join(values)
