"""
3.1 Rounding Numerical Values
Problem
You want to round a floating-point number to a fixed number of decimal places.

Solution
For simple rounding, use the built-in round(value, ndigits) function.
"""

print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25534, 3))

"""
When a value is exactly halfway between two choices, the behavior of round is to round
to the nearest even digit. That is, values such as 1.5 or 2.5 both get rounded to 2.

The number of digits given to round() can be negative, in which case rounding takes
place for tens, hundreds, thousands, and so on.
"""
print(round(1.5))
print(round(2.5))
print(round(3.5))

"""
The number of digits given to round() can be negative, in which case rounding takes
place for tens, hundreds, thousands, and so on. For example:
"""
a = 1627731
print(round(a, -1))  # tens
print(round(a, -2))  # hundreds
print(round(a, -3))  # thousands

"""
Don’t confuse rounding with formatting a value for output. If your goal is simply to
output a numerical value with a certain number of decimal places, you don’t typically
need to use round(). Instead, just specify the desired precision when formatting.
"""
x = 1.23456
print(format(x, "0.2f"))  # 1.23
print(format(x, "0.3f"))  # 1.235
