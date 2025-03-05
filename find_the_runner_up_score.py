# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.
# Input Format:
#   The first line contains n. The second line contains an array A[] of n integers each separated by a space.
# Constraints
#   2 <= n <= 10
#   -100 <= A[i] <= 100
# Output Format: Print the runner-up score.

n = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)

while max_score in scores:
    scores.remove(max_score)

runner_up = max(scores)

print(runner_up)