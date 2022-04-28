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


class Node2:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node2({!r})".format(self._value)

    def add_child(self, other_node):
        self._children.append(other_node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    """Depth-first traversal"""

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # Return myself if just started, create an iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node

        # If processing a child, return its next item
        elif self._child_iter:
            try:
                next_child = next(self._child_iter)
                return next_child
            except StopIteration:
                self._child_iter = None
                return next(self)

        # Advance to the next child and start its iteration
        else:
            self._child_iter = next(self._children_iter).depth_first()


"""
The DepthFirstIterator class works in the same way as the generator version, but it’s
a mess because the iterator has to maintain a lot of complex state about where it is in
the iteration process. Frankly, nobody likes to write mind-bending code like that. Define
your iterator as a generator and be done with it.
"""

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
