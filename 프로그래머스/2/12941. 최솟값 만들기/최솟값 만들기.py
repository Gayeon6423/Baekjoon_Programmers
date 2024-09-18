def solution(A,B):
    ans = 0
    A.sort(reverse=True) # 내림차순
    B.sort() # 오름차순
    for i in range(len(A)):
        ans += A[i] * B[i] # 가장 큰수와 작은 수 곱한 후 누적 합
    return ans
