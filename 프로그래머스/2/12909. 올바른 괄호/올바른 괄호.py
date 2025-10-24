# ( ) 가 짝이 되어야 올바른 괄호
# 스택에는 ( 만 넣어놓고 )가 들어올 때에만 삭제
# 스택 비어있는데 )가 들어오면 false 반환
# for문 다 돌았는데 stack에 ( 남아있으면 false 반환

def solution(s):
    stack = []
    for i in s:
        # 문자열 s 크기만큼 반복
        if i == '(':
            # (가 나오면 stack에 추가
            stack.append(i)
        elif i == ')':
            if stack == []:
                # stack 비어있는데 )가 나오면
                return False
            else:
                # stack에 있는 ( 삭제
                stack.pop()
    if stack != []:
        # for문 끝났는데 stack 비어있지 않다면
        return False
    return True

# def solution(s):
#     stack = []
#     for i in s:
#         if i == '(':
#             stack.append(i)
#         else i == ')':
#             if stack == []:
#                 return False
#             else:
#                 stack.pop()