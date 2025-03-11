# You are given a string.
# Split the string on a " " (space) delimiter and join using a - hyphen.
# Example:
#   >>> a = "this is a string"
#   >>> a = a.split(" ") # a is converted to a list of strings.
#   >>> print a
#   ['this', 'is', 'a', 'string']
# Joining a string is simple:
#   >>> a = "-".join(a)
#   >>> print a
#   this-is-a-string
# Input Format
#   The one line contains a string consisting of space separated words.

s = input()
result = "-".join(s.split())
print(result)
