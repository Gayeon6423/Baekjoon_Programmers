word = input().upper()
word_dict = {}
for alp in word:
    word_dict[alp] = 0
for alp in word:
    word_dict[alp] += 1
max_value = max(word_dict.values())
max_key = [key for key, value in word_dict.items() if value == max_value]


if len(max_key) == 1:
    print(max_key[0])
else:
    print('?')