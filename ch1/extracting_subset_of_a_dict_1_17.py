"""
1.17 Extracting a Subset of a dictionary
Problem
    You want to make a dictionary that is a subset of another
    dictionary.

Solution
    This is easily accomplished using a dictionary comprehension.
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Make a dictionary of all prices over 200
prices_over_200 = {key: value for key, value in prices.items() if value > 200}
print(prices_over_200)
# Make a dictionary of all prices below 200
prices_below_200 = {key: value for key, value in prices.items() if value < 200}
print(prices_below_200)

# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)


"""
Much of what can be accomplished with a dictionary comprehension might also
be done by creating a sequence of tuples and passing them to the 
dict() function.

Slower than the dictionary comprehension approach.
"""
p3 = dict((key, value) for key, value in prices.items() if value > 200)
print(p3)

# Make a dictionary of tech stocks
p4 = {key: prices[key] for key in prices.keys() & tech_names}

