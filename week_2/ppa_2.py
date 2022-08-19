"""
piece-wise fuction
"""

num = float(input())

if 0 < num < 10:
    output = num + 2
elif num >= 10:
    output = num ** 2 + 2
else:
    output = 0

print(output)
