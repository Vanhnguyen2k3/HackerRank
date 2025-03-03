# The provided code stub reads an integer, n, from STDIN.
# For all non-negative integers i<n, print i^2.
# Input Format: The first and only line contains the integer, n.
# Constraints: 1 <= n <= 20
#Output Format: Print n lines, one corresponding to each i.

n = int(input("Nhap so nguyen: "))

for i in range(n):
    print(i ** 2)
