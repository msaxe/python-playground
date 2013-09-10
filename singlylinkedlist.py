#!/usr/bin/env python
# coding: utf-8


class Node(object):
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class LinkedList(object):
    """A singly linked list implementation in Python.

        >>> l = LinkedList()
        >>> l.insert(1)
        >>> l.insert(4)
        >>> l.insert(11)
        >>> l.insert(7)
        >>> l.insert(1)
        >>> print l
    """

    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, x):
        if self.first is None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)

            self.last.next = current
            self.last = current

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = []

            while current.next is not None:
                current = current.next
                out.append(str(current.value))

            return ', '.join(out)
        return 'Empty.'

    def clear(self):
        self.first = None
        self.last = None
