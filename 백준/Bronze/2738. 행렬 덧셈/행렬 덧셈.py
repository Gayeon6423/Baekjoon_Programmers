N,M = map(int, input().split())

A = []
B = []
# 행렬 생성
for i in range(N):
    A.append(list(map(int, input().split())))
for i in range(N):
    B.append(list(map(int, input().split())))
# 행렬 합
for i in range(N): # 행 반복
    sum = []
    for j in range(M): # 열 반복
        sum.append(A[i][j] + B[i][j]) # 원소별 합
    print(*sum)