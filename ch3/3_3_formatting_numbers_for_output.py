"""
3.3. Formatting Numbers for Output
Problem
    You need to format a number for output, controlling the number of digits, alignment,
    inclusion of a thousands separator, and other details.

Solution
    To format a single number for output, use the built-in format() function.
"""

x = 1234.56789


def format_nums1():
    # Two decimal places of accuracy
    print(format(x, "0.2f"))  # 1234.57

    # Right justified in 10 chars, one-digit accuracy
    print(format(x, ">10.1f"))  # '    1234.6'

    # Left justified
    print(format(x, "<10.1f"))  # '1234.6    '

    # Centered
    print(format(x, "^10.2f"))  # '  1234.57  '

    # Inclusion of thousands separator
    print(format(x, ","))  # 1,234.56789
    print(format(x, "0,.2f"))  # 1,234.57

    # Exponential notation e or E
    print(format(x, "e"))  # 1.234568e+03
    print(format(x, "E"))  # 1.234568E+03

    print("The value is {:0,.2f}".format(x))
    print("*" * 20)


def format_nums2():
    """
    Discussion
        Formatting numbers for output is usually straightforward. The technique shown works
        for both floating-point numbers and Decimal numbers in the decimal module.
        When the number of digits is restricted, values are rounded away according to the same
        rules of the round() function. For example:
    """
    print(format(x, "0.1f"))
    print(format(-x, "0.2f"))  # -1234.57
    print("*" * 20)


def format_nums_locale_aware():
    """
    Formatting of values with a thousands separator is not locale aware. If you need to take
    that into account, you might investigate functions in the locale module. You can also
    swap separator characters using the translate() method of strings. For example:
    :return:
    """
    swap_separators = {
        ord("."): ",",
        ord(","): "."
    }
    print(format(x, ",").translate(swap_separators))
    print("*" * 20)


def format_w_modulo():
    """
    numbers are formatted using the % operator. This formatting it's still acceptable but less
    powerful than the format() method.
    """
    print("%0.2f" % x)
    print("%10.1f" % x)
    print("%-10.1f" % x)


if __name__ == "__main__":
    format_nums1()
    format_nums2()
    format_nums_locale_aware()
    format_w_modulo()
