"""
Accept two positive integers x and y as input. Print the number of digits in
x^y.
"""

x = int(input())
y = int(input())

exp = x ** y
print(len(str(exp)))
