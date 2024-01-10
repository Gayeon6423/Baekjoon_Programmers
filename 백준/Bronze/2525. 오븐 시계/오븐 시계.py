A,B = map(int, input().split())
C = int(input())

def solution(A,B,C):
    if B+C < 60: 
        A = A 
        B = B + C 
    elif B+C >= 60:
        if A + ((B+C) // 60) < 24:
            A = A + ((B+C) // 60) 
            B = (B+C) - 60 * ((B+C) // 60) 
        else:
            A = A + ((B+C) // 60) - 24 
            B = (B+C) - 60 * ((B+C) // 60) 
    print(A,B)

solution(A, B, C)