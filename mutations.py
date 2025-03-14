# Read a given string,
# change the character at a given index and then print the modified string.
# Function Description
#   Complete the mutate_string function in the editor below.
#   mutate_string has the following parameters:
#       string string: the string to change
#       int position: the index to insert the character at
#       string character: the character to insert
# Returns
#   string: the altered string
# Input Format
#   The first line contains a string, string.
#   The next line contains an integer position,
#   the index location and a string character, separated by a space.

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

# Read input values
s = input()   # Original string
i, c = input().split()  # Read index and character
i = int(i)  # Convert index to integer

# Call function and print the modified string
print(mutate_string(s, i, c))