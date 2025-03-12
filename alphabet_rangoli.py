# You are given an integer, N.
# Your task is to print an alphabet rangoli of size N.
# (Rangoli is a form of Indian folk art based on creation of patterns.)
# Input Format
#   Only one line of input containing size, the size of the rangoli.
# Constraints
#   0 < size <27

import string

def print_rangoli(n):
    alphabet = string.ascii_lowercase
    width = 4 * n - 3
    lines = []

    for i in range(n):
        letters = "-".join(alphabet[n - 1:i:-1] + alphabet[i:n])
        lines.append(letters.center(width, "-"))

    print("\n".join(lines + lines[-2::-1]))


n = int(input().strip())
print_rangoli(n)
