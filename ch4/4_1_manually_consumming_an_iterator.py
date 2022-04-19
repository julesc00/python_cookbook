"""
4.1. Manually Consuming an Iterator

Problem
    You need to process items in an iterable, but for whatever reason, you can’t or don’t want
    to use a for loop.
Solution
    To manually consume an iterable, use the next() function and write your code to catch
    the StopIteration exception. For example, this example manually reads lines from a
    file:
"""


def pass_iterator():
    with open("/etc/passwd") as f:
        try:
            while True:
                line = next(f)
                print(line, end="")
        except StopIteration:
            pass


def pass_iterator2():
    with open("/etc/passwd") as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end="")


if __name__ == "__main__":
    # pass_iterator()
    pass_iterator2()
