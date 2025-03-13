# You are given a date. Your task is to find what the day is on that date.
# Input Format
#   A single line of input containing the space separated month, day and year, respectively,
#   in MM DD YYYY format.
# Constraints
#   2000 < year < 3000
# Output Format
#   Output the correct day in capital letters.

import calendar

def find_day(month, day, year):
    weekday_index = calendar.weekday(year, month, day)

    return calendar.day_name[weekday_index].upper()

month, day, year = map(int, input().split())

print(find_day(month, day, year))
