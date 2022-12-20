#!/usr/bin/python3
"""
Defines a Singly Linked List
"""


class Node:
    """
    This is a class that defines a node in a linked list
    """

    def __init__(self, data: int, next_node=None) -> None:
        """
        __init__ initialises a Node instance

        Args:
            data (int): data to be stored in the node
            next_node (Node, optional): pointer to next node.
                                        Defaults to None.
        """

        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self) -> int:
        """
        data is a getter for the private data instance attribute

        Returns:
            int: the data stored in the node
        """

        return self.__data

    @data.setter
    def data(self, data: int) -> None:
        """
        data is a setter for the private data instance attribute

        Args:
            data (int): the value to store in the node

        Raises:
            TypeError: raised if data is not an integer
        """

        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        self.__data = data

    @property
    def next_node(self):
        """
        next_node is a getter for the private next_node instance attribute

        Returns:
            Node: a pointer to the next node
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """
        next_node is a setter for the private next_node instance attribute

        Args:
            next_node (Node): a pointer to the next node

        Raises:
            TypeError: if next_node is not a Node object
        """

        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = next_node


class SinglyLinkedList:
    """
    This is a class that defines a singly linked list
    """

    def __init__(self) -> None:
        """
        __init__ initialises a linked list object
        """

        self.__head: Node = None

    def sorted_insert(self, value):
        """
        sorted_insert inserts a node in a sorted (ascending) linked list

        Args:
            value (int): data stored in the new node object
        """

        if self.__head is None:
            self.__head = Node(data=value)
            return

        if value < self.__head.data:
            self.__head = Node(data=value, next_node=self.__head)
            return

        current: Node = self.__head

        while current.next_node is not None:
            if value < current.next_node.data:
                temp: Node = current.next_node
                current.next_node = Node(data=value, next_node=temp)
                return
            current = current.next_node

        current.next_node = Node(data=value)

    def __str__(self) -> str:
        """
        __str__ defines linkedlist representation when passed to str()/print()

        Returns:
            str: print() representation
        """

        values = []
        current: Node = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node

        return "\n".join(values)
