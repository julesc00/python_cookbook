"""
4.5. Iterating in Reverse

Problem
    You want to iterate in reverse over a sequence.

Solution
    Use the built-in reversed() function.
"""

A = [1, 2, 3, 4]


def reverse_iterate():
    [print(x) for x in reversed(A)]


def print_file_reverse(filename):
    """
    Be aware that turning an iterable into a list as shown could consume a lot of memory if it's large.
    """
    f = open(filename)
    [print(line, end="") for line in reversed(list(f))]


"""
Many programmers don’t realize that reversed iteration can be customized on user-defined
classes if they implement the __reversed__() method. For example:
"""


class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


if __name__ == "__main__":
    reverse_iterate()
