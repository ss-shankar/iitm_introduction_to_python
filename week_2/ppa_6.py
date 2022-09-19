"""
Accept a string as input. If the input string is of odd length, then continue
with it. If the input string is of even length, make the string of odd length
by following the two steps mentioned below:
    (1) If the last character is a period (.), then remove it
    (2) If the last character is not a period, then add a period (.) to the
    end of the string

Call this string of odd length word. Select a substring made up of three
consecutive characters from word such that there are an equal number of
characters to the left and right of this substring. Print this substring as
output. You can assume that all input strings will be in lower case and will
have a length of at least four.
"""

string = input()

if len(string) % 2 == 0:
    if string[-1] == '.':
        new_string = string[:len(string) - 1]
    else:
        new_string = string + '.'
else:
    new_string = string

start_num = (len(new_string) // 2) - 1
sub_string = new_string[start_num:start_num + 3]

print(sub_string)
