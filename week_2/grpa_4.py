"""
You are given the dates of birth of two persons, not necessarily from the same
family. Your task is to find the younger of the two. If both of them share the
same date of birth, then the younger of the two is assumed to be that person
whose name comes first in alphabetical order.

The input will have four lines. The first two lines correspond to the first
person, while the last two lines correspond to the second person.
For each person, the first line corresponds to the name and the second line
corresponds to the date of birth in DD-MM-YYYY format. Your output should be
the name of the younger of the two.
"""

name_1 = input()
dob_1 = input()
name_2 = input()
dob_2 = input()

if dob_1 == dob_2:
    if name_1 < name_2:
        print(name_1)
    else:
        print(name_2)

year_1 = int(dob_1[6:])
year_2 = int(dob_2[6:])

month_1 = int(dob_1[3:5])
month_2 = int(dob_2[3:5])

day_1 = int(dob_1[:2])
day_2 = int(dob_2[:2])
