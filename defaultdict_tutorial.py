# Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'
#   For the first word in group B, 'a', it appears at positions 1 and 3 in group A.
#   The second word, 'c', does not appear in group A, so print -1.
#   Expected output:
#    1 3
#    -1
# Input Format
#   The first line contains integers, n and m separated by a space.
#   The next n lines contains the words belonging to group A.
#   The next m lines contains the words belonging to group B.
# Constraints
#   1 <= n <= 10000
#   1 <= m <= 100
#   1 <= length of each word in the input <= 100
# Output Format
#   Output m lines.
# The i^th line should contain the 1-indexed positions of the occurrences of the i^th word separated by spaces.

from collections import defaultdict

n, m = map(int, input().split())
group_A = defaultdict(list)

for i in range(1, n + 1):
    word = input().strip()
    group_A[word].append(i)

for _ in range(m):
    word = input().strip()
    if word in group_A:
        print(*group_A[word])
    else:
        print(-1)
