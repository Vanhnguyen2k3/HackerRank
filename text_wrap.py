# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.
# Input Format
#   The first line contains a string, string.
#   The second line contains the width, max_width.
# Constraints
#   0 < len(string) < 1000
#   0 < max_width < len(string)

import textwrap

def wrap(string, width):
    return textwrap.fill(string, width)

s = input().strip()
w = int(input().strip())

print(wrap(s, w))