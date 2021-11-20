
"""
You want to keep a limited history of the last few items seen during iteration or during some other
kind of processing.
"""

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == "__main__":
    with open("some_file.txt") as f:
        for line, prev_lines in search(f, "python", 5):
            for p_line in prev_lines:
                print(p_line, end="")
            print(line, end="")
            print("_" * 20)
