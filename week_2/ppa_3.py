"""
Accpect integer as input and print time of the day as output
"""

time = int(input())

if time < 0
    print("INVALID")
elif 0 <= time <= 5:
    print("NIGHT")
elif 6 <= time <= 11:
    print("MORNING")
elif 12 <= time <= 17:
    print("AFTERNOON")
elif 18 <= time <= 23:
    print("EVENING")
else:
    print("INVALID")
