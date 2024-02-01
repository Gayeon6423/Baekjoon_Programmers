# 풀이1 : 메모리 초과
# X = int(input())
# loop_num = 1

# # 분자 리스트 생성
# numerator_li = []
# while len(numerator_li) < X:
#     numerator_li.append([i for i in range(1,loop_num)])
#     loop_num += 1
# numerator_li.remove([])

# # 분자 하부 리스트 정렬 
# tmp = []
# for index, li in enumerate(numerator_li):
#     if index % 2 != 0: # 홀수번째면 그대로
#         tmp.append(li)
#     else: # 짝수번째면 역정렬
#         tmp.append(li[::-1])        
# numerator_li = tmp

# # 분모 리스트 생성
# denominator_li = []
# for li in numerator_li:
#     denominator_li.append(li[::-1])

# # 분수 생성
# tmp_fraction_li = []
# fraction_li = []

# for i in range(len(numerator_li)):
#     for j in range(len(denominator_li[i])):
#         tmp_fraction_li.append(str(numerator_li[i][j]) + '/' + str(denominator_li[i][j]))
#     fraction_li.append(tmp_fraction_li)

# fraction_li = fraction_li[0]

# print(fraction_li[X-1])

# 풀이2
# 몇 번째 줄에 몇 번째 위치의 분수인지 파악
X = int(input())
line = 1
while X > line:
    X -= line
    line += 1

# 짝수 라인 : 분모 +1, 분자 -1 
if line % 2 == 0:
    numerator = X
    denominator = line - X + 1
# 홀수 라인 : 분모 -1, 분자 +1
elif line % 2 == 1:
    numerator = line - X + 1
    denominator = X
print(f'{numerator}/{denominator}')