A,B = map(int, input().split())

def solution(A,B):
    if A > B:
        print('>')
    elif A < B:
        print('<')
    else:
        print('==')

solution(A,B)
