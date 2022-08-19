sequence = input().split(',')

count_list = []
for i in range(len(sequence)):
    count = 1
    new_list = sequence[i:]
    for j in range(len(new_list) - 1):
        word_1 = new_list[j]
        word_2 = new_list[j+1]
        if word_1[-1] == word_2[0]:
            count += 1
            if j == (len(new_list) - 2):
                count_list.append(count)
        else:
            count_list.append(count)
            break

print(max(count_list))
