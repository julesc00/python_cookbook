"""
Problem
You want to implement a queue that sorts items by a given priority and always returns
the item with the highest priority on each pop operation.

Solution
The following class uses the heapq module to implement a simple priority queue:
"""
import heapq
import queue


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


q = PriorityQueue()
q.push(Item("foo"), 1)
q.push(Item("bar"), 5)
q.push(Item("spam"), 4)
q.push(Item("grok"), 1)

# According to PriorityQueue class and its method pop, it'll pop the last highest item.
print(q.pop())  # Item('bar')
print(q.pop())  # Item('spam')
print(q.pop())  # Item('foo'); This were popped according to the order they were inserted.
print(q.pop())  # Item('grok')
print(q)

