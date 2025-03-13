# Now, let's use our knowledge of sets and help Mickey.
# Ms. Gabriel Williams is a botany professor at District College.
# One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
# Formula used: Average = Sum of Distinct Heights / Total Number of Distinct Heights
# Input Format
#   The first line contains the integer, N, the size of arr.
#   The second line contains the N space-separated integers, arr[i].
# Constraints
#   0 < N <= 100

def average_height(arr):
    distinct_heights = set(arr)
    return sum(distinct_heights) / len(distinct_heights)

n = int(input().strip())
heights = list(map(int, input().split()))

print(average_height(heights))
