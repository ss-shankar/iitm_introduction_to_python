"""
Accept a string as input and print the vowels present in the string in
alphabetical order. If the string doesn't contain any vowels, then print the
string none as output. Each vowel that appears in the input string
irrespective of its case should appear just once in lower case in the output
"""

string = input().lower()
vowels = 'aeiou'

vowels_list = []
for i in vowels:
    if i in string:
        vowels_list.append(i)

if len(vowels_list) == 0:
    print("none")
else:
    print(''.join(vowels_list))
