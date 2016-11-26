# Skeleton file for the Python "linked-list" exercise.


class Node(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None

    def pop(self):
        if self.last is None:
            raise ValueError()

        retValue = self.last.value
        self.last = self.last.prev
        return retValue

    def push(self, value):
        # check if list is empty
        if self.first is None and self.last is None:
            n = Node(value)
            self.first = n
            self.last = n
            return

        # add the node to end
        n = Node(value)
        self.last.next = n
        n.prev = self.last
        self.last = n

    def shift(self):
        if self.first is None:
            raise ValueError()

        retValue = self.first.value
        self.first = self.first.next
        return retValue

    def unshift(self, value):
        # check if list is empty
        if self.first is None and self.last is None:
            n = Node(value)
            self.first = n
            self.last = n
            return

        # add the node to beginning
        n = Node(value)
        self.first.prev = n
        n.next = self.first
        self.first = n