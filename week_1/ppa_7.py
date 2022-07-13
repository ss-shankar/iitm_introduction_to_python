"""
Accept a five digit number as input and print the sum of its digits as output.
"""
number_list = list(input())
sum = 0
for i in number_list:
    sum = sum + int(i)

print(sum)
