# 의상의 종류를 key로 하는 딕셔너리 만드는 것이 핵심
# 종류별로 의상을 나눠 저장한 딕셔너리 closet 가지고 경우의 수 계산
# A의 종류가 N개, B의 종류가 M개 일 때 가능한 모든 경우의 수는 (N+1)(M+1)로 구할 수 있다. 

# def solution(clothes):
#     # 각 종류별 가진 의상을 저장(카테고리:[이름,이름,...])
#     closet = {}
#     for name, cat in clothes:
#         if cat not in closet:
#             closet[cat] = []
#         closet[cat].append(name)
#     # A의 종류가 N개, B의 종류가 M개 일 때 가능한 모든 경우의 수 (N+1)(M+1)
#     # (N+1)(M+1) = NM + N + M + 1
#     ans = 1
#     for _, value in closet.items():
#         ans = ans * (len(value) + 1)
#     # 아무것도 안 입는 경우를 제외하기 위해 -1
#     ans  = ans - 1
#     return ans

def solution(clothes):
    closet = {}
    for name, cat in clothes:
        if cat not in closet:
            closet[cat] = []
        closet[cat].append(name)
    ans = 1
    for _, value in closet.items():
        ans = ans * (len(value) + 1)
    ans = ans - 1
    return ans

def solution(clothes):
    # 옷장 해시 테이블
    closet = {}
    for name, cat in clothes:
        # print(name, cat)
        if cat not in closet:           
            # 카테고리가 옷장 테이블에 없다면 카테고리 새롭게 추가
            closet[cat] = []
        # 카테고리가 항목 추가
        closet[cat].append(name)
    # 옷 조합 기본 수
    ans = 1
    # 조합의 수 = (n+1) * (m+1) * (z+1) * '''
    # 조합의 수 = 조합의 수 - 1(전체)
    for key,value in closet.items():
        ans = ans * (len(value)+1)
    ans = ans - 1
    return ans
