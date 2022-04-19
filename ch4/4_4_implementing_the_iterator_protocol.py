"""
4.4. Implementing the Iterator Protocol

Problem
    You are building custom objects on which you would like to support iteration, but would
    like an easy way to implement the iterator protocol.

Solution
    By far, the easiest way to implement iteration on an object is to use a generator function.
    In Recipe 4.2, a Node class was presented for representing tree structures. Perhaps you
    want to implement an iterator that traverses nodes in a depth-first pattern. Here is how
    you could do it:
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)

    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    [print(ch) for ch in root.depth_first()]
