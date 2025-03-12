# Given an integer, n, print the following values for each integer i from 1 to n:
#   1. Decimal
#   2. Octal
#   3. Hexadecimal (capitalized)
#   4. Binary
# Input Format
#   A single integer denoting n.
# Constraints
#   1 <= n <= 99

def print_formatted(n):
    width = len(bin(n)[2:])  # Calculate the width based on the binary length

    for i in range(1, n + 1):
        decimal = str(i)
        octal = oct(i)[2:]  # Convert to octal and remove '0o'
        hexadecimal = hex(i)[2:].upper()  # Convert to hex, remove '0x', and capitalize
        binary = bin(i)[2:]  # Convert to binary and remove '0b'

        # Print with right alignment
        print(decimal.rjust(width), octal.rjust(width), hexadecimal.rjust(width), binary.rjust(width))


# Read input
n = int(input().strip())
print_formatted(n)