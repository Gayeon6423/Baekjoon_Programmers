H,M = map(int, input().split())

def solution(H,M):
    if M >= 45:
        M = M - 45
        H = H
    else:
        M = M - 45 + 60
        if H == 0: # 자정이면
            H = 23
        else:
            H = H-1
    print(H,M)

solution(H,M)