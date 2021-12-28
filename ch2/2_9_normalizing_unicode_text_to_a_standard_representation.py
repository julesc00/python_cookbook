"""
2.9. Normalizing Unicode Text to a Standard Representation

Problem
    You’re working with Unicode strings, but need to make sure that all of the strings have
    the same underlying representation.

Solution
    In Unicode, certain characters can be represented by more than one valid sequence of
    code points.
"""
import unicodedata

s1 = "Spicy Jalape\u00f1o"  # Spicy Jalapeño
s2 = "Spicy Jalapen\u0303o"  # Spicy Jalapeño
print(s1 == s2)
print(s1)

# Normalize the text
# NFC
# means that characters should be fully composed (i.e., use a single code point if possible).
t1 = unicodedata.normalize("NFC", s1)

# NFD means that characters should be fully decomposed with the use of combining characters.
t2 = unicodedata.normalize("NFD", s2)
print(t1 == t2)
print(t1)
print(ascii(t2))

s3 = "\ufb01"  # A single character
print(s3)
n_s3 = unicodedata.normalize("NFD", s3)
print(n_s3)  # ﬁ

# Notice how the combined letters are broken apart here
n_two_ltrs = unicodedata.normalize("NFKD", s3)
print(n_two_ltrs)  # fi


"""
Suppose you want to remove all diacritical marks from some text (possibly for the purposes
of searching or matching):
"""
t3 = unicodedata.normalize("NFD", s2)
cleaned_string = "".join(c for c in t3 if not unicodedata.combining(c))
print(cleaned_string)  # Spicy Jalapeno
