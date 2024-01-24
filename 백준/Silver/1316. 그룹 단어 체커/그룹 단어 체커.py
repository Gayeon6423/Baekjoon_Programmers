N = int(input())
word_li = []
for _ in range(N):
    word = input()
    word_li.append(word)

# 연속 단어 처리(연속되는 단어 제거)
uncontinuous_word_li = []
for word in word_li:
    uncontinuous_word = word[0] 
    for index in range(1, len(word)):
        if word[index] != word[index - 1]:
            uncontinuous_word += word[index]
    uncontinuous_word_li.append(uncontinuous_word)
        
# 중복 단어 처리(다시 나온 단어 제거)
process_word_li = []
for uncontinuous_word in uncontinuous_word_li:
    unique_word = ''
    for alp in uncontinuous_word:
        if alp not in unique_word:
            unique_word += alp
    process_word_li.append(unique_word)

# 그룹 아닌 단어 개수 출력(연속 처리 단어 중 중복 제거한 단어만 제외)
count = 0
for index, word in enumerate(process_word_li):
    if process_word_li[index] == uncontinuous_word_li[index]:
        count += 1

print(count)