"""
Accept a sequence of five single digit numbers separated by commas as input.
Print the product of all five numbers.
"""
numbers_list = input().split(',')

product = 1
for i in numbers_list:
    product = product * int(i)

print(product)
