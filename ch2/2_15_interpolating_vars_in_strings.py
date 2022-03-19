"""
2.15. Interpolating Variables in Strings
Problem:
    You want to create a string in which embedded variable names are substituted with a string representation
    of a variable’s value.

Solution:
    Python has no direct support for simply substituting variable values in strings. However, this feature can be
    approximated using the format() method of strings.
"""
import sys


s = "{name} has {n} messages."
# This is ok if you want to define those variables on-the-fly.
print(s.format(name="Julito", n=23))


def welcome_user(msg):
    return msg.format(user="cesarito".capitalize())


"""
Alternatively, if the values to be substituted are truly found in variables, you can use the
combination of format_map() and vars()
"""
name = "Jemima"
n = 23
print(s.format_map(vars()))


# Another similar example
def show_n_msgs(nombre, msgs):
    msg = "{nombre} has {msgs} messages."
    return msg.format_map(vars())


# One subtle feature of vars() is that it also works with instances.
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info("Claudia", 676)
print(s.format_map(vars(a)))


"""
One downside of format() and format_map() is that they do not deal gracefully with
missing values.

One way to avoid this is to define an alternative dictionary class with a __miss
ing__() method
"""


class Safesub(dict):
    def __missing__(self, key):
        return "{" + key + "}"


del n
print(s.format_map(Safesub(vars())))  # Jemima has {n} messages.


"""
If you find yourself frequently performing these steps in your code, you could hide the
variable substitution process behind a small utility function that employs a so-called
“frame hack.”
"""


def sub(text):
    return text.format_map(Safesub(sys._getframe(1).f_locals))


if __name__ == "__main__":
    welcome_msg = "Welcome back {user}!"
    print(welcome_user(welcome_msg))
    print("*"*32)

    name2 = "Michelina"
    n2 = 53
    print(show_n_msgs(name2, n2))
    print(sys.platform)
