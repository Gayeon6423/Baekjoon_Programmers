# 의상의 종류를 key로 하는 딕셔너리 만드는 것이 핵심
# 종류별로 의상을 나눠 저장한 딕셔너리 closet 가지고 경우의 수 계산
# A의 종류가 N개, B의 종류가 M개 일 때 가능한 모든 경우의 수는 (N+1)(M+1)로 구할 수 있다. 

def solution(clothes):
    # 각 종류별 가진 의상을 저장(카테고리:[이름,이름,...])
    closet = {}
    for name, cat in clothes:
        if cat not in closet:
            closet[cat] = []
        closet[cat].append(name)
    # A의 종류가 N개, B의 종류가 M개 일 때 가능한 모든 경우의 수 (N+1)(M+1)
    # (N+1)(M+1) = NM + N + M + 1
    ans = 1
    for _, value in closet.items():
        ans = ans * (len(value) + 1)
    # 아무것도 안 입는 경우를 제외하기 위해 -1
    ans  = ans - 1
    return ans