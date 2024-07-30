def solution(citations):
    citations.sort(reverse=True) # 내리차순 정렬
    h=0
    for idx, max_cit in enumerate(citations):
        if idx + 1 <= max_cit: # i+1번째 논문이 i+1번 미만으로 인용될 경우
            h = idx + 1 # H-Index 후보로 탐색
        elif idx + 1 > max_cit: # i+1번째 논문이 i+1번 이상 인용될 경우
            break # H-Index 반환
        print(max_cit, h)
    return h