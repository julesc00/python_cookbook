"""
3.2. Performing Accurate Decimal Calculations

Problem
    You need to perform accurate calculations with decimal numbers, and don’t want the
    small errors that naturally occur with floats.

Solution
    A well-known issue with floating-point numbers is that they can’t accurately represent
    all base-10 decimals. Moreover, even simple mathematical calculations introduce small
    errors.
"""
from decimal import Decimal
from decimal import localcontext
import math


def using_decimal():
    a = 4.2
    b = 2.1
    print(a + b)
    print((a + b) == 6.3)  # False

    # With Decimal, they're declared as strings, but act as numbers
    c = Decimal("4.2")
    d = Decimal("2.1")
    print(type(c))
    print(c + d)
    print((c + d) == Decimal("6.3"))  # True


def decimal_rounding():
    """
    A major feature of decimal is that it allows you to control different aspects of calculations,
    including number of digits and rounding. To do this, you create a local context
    and change its settings. For example:

    Note:
        All of this said, the main use of the decimal module is in programs involving things
        such as finance. In such programs, it is extremely annoying to have small errors creep
        into the calculation. Thus, decimal provides a way to avoid that. It is also common to
        encounter Decimal objects when Python interfaces with databases—again, especially
        when accessing financial data.
    """
    a = Decimal("1.3")
    b = Decimal("1.7")

    print(a / b)

    with localcontext() as ctx:
        ctx.prec = 3
        print(a / b)  # 0.765

    with localcontext() as ctx:
        ctx.prec = 50
        print(a / b)  # 0.76470588235294117647058823529411764705882352941176


def adding_large_and_small_nums():
    """
    However, for other algorithms, you really need to study the algorithm and understand
    its error propagation properties.
    """
    nums = [1.23e+18, 1, 1.23e+18]
    print(sum(nums))

    # More accurate implementation in math.fsum(), though I get the same result in both prints.
    print(math.fsum(nums))


if __name__ == "__main__":
    using_decimal()
    decimal_rounding()
    adding_large_and_small_nums()
