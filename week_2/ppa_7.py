"""
A sequence of five words is called magical if the  i word is a substring of the
(i + 1) word for every i in the range 1<= i < 5.
 Accept a sequence of five words as input, one word on each line.
 Print magical if the sequence is magical and non-magical otherwise.

Note that str_1 is a substring of str_2 if and only if str_1 is present as a
sequence of consecutive characters in str_2.
"""
words_list = []
for i in range(5):
    words_list.append(input())

for i in range(4):
    if words_list[i] in words_list[i+1]:
        flage = True
    else:
        flage = False
        break

if flage:
    print("magical")
else:
    print("non-magical")
