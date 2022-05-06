"""
4.8. Skipping the First Part of an Iterable

Problem
    You want to iterate over items in an iterable, but the first few items aren’t of interest,
    and you just want to discard them.

Solution
    The itertools module has a few functions that can be used to address this task. The
    first is the itertools.dropwhile() function. To use it, you supply a function and an
    iterable. The returned iterator discards the first items in the sequence as long as the
    supplied function returns True. Afterward, the entirety of the sequence is produced.
    To illustrate, suppose you are reading a file that starts with a series of comment lines.

    with open('/etc/passwd') as f:
    ... for line in f:
.   .. print(line, end='')
    ...
    ##
    # User Database
    #
    # Note that this file is consulted directly only when the system is running
    # in single-user mode. At other times, this information is provided by
    # Open Directory.
    ...
    ##
    nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
    root:*:0:0:System Administrator:/var/root:/bin/sh
    ...

    If you want to skip all of the initial comment lines, here’s one way to do it:
"""
from itertools import dropwhile, islice


def skip_items():
    with open("/etc/passwd") as f:
        for line in dropwhile(lambda l: l.startswith("#"), f):
            print(line, end="")


def skip_known_items():
    """
    If you
    happen to know the exact number of items you want to skip, then you can use iter
    tools.islice() instead.
    """
    items = ["a", "b", "c", 1, 4, 10, 15]
    [print(x) for x in islice(items, 3, None)]


def skip_items2():
    """
    The dropwhile() and islice() functions are mainly convenience functions that you
    can use to avoid writing rather messy code such as this:
    """
    with open("/etc/passwd") as f:
        # Skip over initial comments
        while True:
            line = next(f, "")
            if not line.startswith("#"):
                break

        while line:
            # Replace with useful processing
            print(line, end="")
            line = next(f, None)


def skip_items3():
    """
    Refactoring the previous code.
    """
    with open("/etc/passwd") as f:
        lines = (line for line in f if not line.startswith("#"))
        [print(line, end="") for line in lines]


if __name__ == "__main__":
    # skip_known_items()
    # skip_items2()
    skip_items3()
