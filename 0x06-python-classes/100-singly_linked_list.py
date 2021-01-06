#!/usr/bin/python3
""" Module: For creating a singly linked list in Python. """


class Node:
    """ Class: For creating Node objects. """
    def __init__(self, data, next_node=None):
        """ __init__:

        Args:
            data (int): Data contained inside the Node instance.
            next_node (attribute): to point to the next Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Method: For getting the data from the node. """
        return self.__data

    @data.setter
    def data(self, value):
        """ Method: For setting the data in the node.

        Args:
            value: Data value to set into the node.
        """
        if type(value) is int:
            self.__data = value  #: Set pirvate data value.
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ Method: For getting the next_node of the instance Node. """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Method: For setting the next_node's data value.

        Args:
            value: Data value to set into the next_node.
        """
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ Class: For creating the sinlgy linked list object. """
    def __init__(self):
        """ __init__: """
        self.__head = None  #: Set init head.

    def sorted_insert(self, value):
        """ sorted_insert: Inserts a node on the linked list in ascending order.

        Args:
            value: Value of the data for the new node.
        """
        tmp = self.__head
        new_node = Node(value)

        if tmp is None:
            self.__head = new_node

        elif value < tmp.data:
            new_node.next_node = self.__head
            self.__head = new_node

        else:
            while tmp.next_node and value > tmp.next_node.data:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """ Method: For printing the linked list. """
        tmp = self.__head
        list_string = ""
        if tmp:
            while tmp:
                list_string += str(tmp.data) + "\n"
                tmp = tmp.next_node
        return list_string[0: -1]
