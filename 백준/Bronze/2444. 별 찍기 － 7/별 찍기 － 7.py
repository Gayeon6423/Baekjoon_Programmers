N = int(input())
B = []

for i in range(1, N * 2, 2):
    star = '*' * i
    B.append(star) # 별 추가

for i in range(len(B)):
    print(' ' * (N - i - 1) + B[i])

B.reverse()

for i in range(1, len(B)):
    print(' ' * i + B[i])
