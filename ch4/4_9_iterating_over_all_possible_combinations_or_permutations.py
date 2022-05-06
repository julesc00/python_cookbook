"""
Problem
    You want to iterate over all of the possible combinations or permutations of a collection
    of items.

Solution
    The itertools module provides three functions for this task. The first of these—iter
    tools.permutations()—takes a collection of items and produces a sequence of tuples
    that rearranges all the items into all possible permutations (i.e., it shuffles them into
    all possible configurations).

Tip:
    Permutation are different in that they consider the order of elements, while combinations not.
"""
from itertools import permutations, combinations, combinations_with_replacement

items = [1, "a", 2, "b", 3, "c", 4, "d"]


def iter_possible_permutations():

    [print(p) for p in permutations(items)]


def iter_possible_combinations():
    [print(c) for c in combinations(items, 3)]


def shuffler2():
    counter = 0
    [print(p) for p in permutations(items)]

    # All permutations of a smaller length, give the optional argument.
    for _ in permutations(items, 2):
        counter += 1
    print(counter)


def permutate_year():
    year = [n for n in "1977"]
    [print(f"19{p}") for p in permutations(year, 2)]


def iter_combination_w_replace():
    """
    When producing combinations, chosen items are removed from the collection of possible
    candidates (i.e., if 'a' has already been chosen, then it is removed from consideration).
    The itertools.combinations_with_replacement() function relaxes this, and
    allows the same item to be chosen more than once.
    """
    lst = ["a", "b", "c"]
    [print(c) for c in combinations_with_replacement(lst, 3)]


if __name__ == "__main__":
    # iter_possible_permutations()
    # shuffler2()
    # iter_possible_combinations()
    # permutate_year()
    iter_combination_w_replace()
