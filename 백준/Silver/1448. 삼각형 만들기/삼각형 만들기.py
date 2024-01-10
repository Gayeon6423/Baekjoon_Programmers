#삼각형 만들기(그리디)
import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)] #문자열 n줄 입력받아 리스트로
A.sort(reverse=True)

answer = -1

# 그 어떤 삼각형도 어느 한 변의 길이가 나머지 두 변의 길이를 합한 것보다 길거나 같을 수 없다.
for i in range(N - 2):
    if A[i] < A[i + 1] + A[i + 2]:
        answer = A[i] + A[i + 1] + A[i + 2]
        break
print(answer)