word_mat = []
for i in range(5):
    word_mat.append(list(map(str, input())))

max_len = max([len(word) for word in word_mat]) # 가장 긴 칼럼 수
tmp_li = []
for i in range(max_len):
    for row, word in enumerate(word_mat):
        if i >= len(word): # 다른 행보다 칼럼수 적으면 통과
            continue
        tmp_li.append(word[i])

for word in tmp_li:
    print(word, end='')