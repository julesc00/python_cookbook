"""
4.3. Creating New Iteration Patterns with Generators

Problem
    You want to implement a custom iteration pattern that’s different than the usual builtin
    functions (e.g., range(), reversed(), etc.).

Solution
    If you want to implement a new kind of iteration pattern, define it using a generator
    function. Here’s a generator that produces a range of floating-point numbers:
"""


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


def countdown(n):
    print("Starting to count from: ", n)
    while n > 0:
        yield n
        n -= 1
    print("Done!")


if __name__ == "__main__":
    [print(n) for n in frange(0, 4, 0.5)]
    print(countdown(5))
    c = countdown(3)
    print(c)
    print(next(c))
    print(next(c))
    print(next(c))

"""
The key feature is that a generator function only runs in response to “next” operations
carried out in iteration. Once a generator function returns, iteration stops. However,
the for statement that’s usually used to iterate takes care of these details, so you don’t
normally need to worry about them.
"""
