"""
4.6. Defining Generator Functions with Extra State
Problem
    You would like to define a generator function, but it involves extra state that you would
    like to expose to the user somehow.

Solution
    If you want a generator to expose extra state to the user, don’t forget that you can easily
    implement it as a class, putting the generator function code in the __iter__() method.
"""

from collections import deque


class LineHistory:
    """
    To use this class, you would treat it like a normal generator function. However, since it
    creates an instance, you can access internal attributes, such as the history attribute or
    the clear() method.
    """
    def __init__(self, lines, history_len=3):
        self.lines = lines
        self.history = deque(maxlen=history_len)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


def file_opener():
    with open("somefile.txt") as f:
        lines = LineHistory(f)
        for line in lines:
            if "python" in line:
                for lineno, hline in lines.history:
                    print(f"{lineno}:{hline}", end="")
