S = str(input())
alp_li = 'abcdefghijklmnopqrstuvwxyz'
output_li = [-1] * 26

for index, word in enumerate(S):
    alp_num = alp_li.index(word)
    if output_li[alp_num] == -1:
        output_li[alp_num] = index

for output in output_li:
    print(output, end = ' ')
