"""
2.12. Sanitizing and Cleaning Up Text
Problem
    Some bored script kiddie has entered the text “pýtĥöñ” into a form on your web page,
    and you’d like to clean it up somehow.

Solution
    The problem of sanitizing and cleaning up text applies to a wide variety of problems
    involving text parsing and data handling. At a very simple level, you might use basic
    string functions (e.g., str.upper() and str.lower()) to convert text to a standard case.
    Simple replacements using str.replace() or re.sub() can focus on removing or changing
    very specific character sequences.
"""
import unicodedata
import sys

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)


# make a small translation table and use translate()
def string_sanitize(s_str: str) -> str:
    remap = {
        ord("\t"): " ",
        ord("\f"): " ",
        ord("\r"): None  # Deleted
    }
    a = s_str.translate(remap)
    cmb_chars = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
    b = unicodedata.normalize("NFD", a)
    cleaned_str = b.translate(cmb_chars)

    return cleaned_str


# Unicode decimal digit chars to their equivalent in ASCII
def uni_to_ascii(s_str: str) -> str:
    digitmap = {
        c: ord("0") + unicodedata.digit(chr(c)) for c in range(sys.maxunicode)
        if unicodedata.category(chr(c)) == "Nd"
    }
    s_translated = s_str.translate(digitmap)
    return s_translated


if __name__ == "__main__":
    x = '\u0661\u0662\u0663'
    print(uni_to_ascii(x))
