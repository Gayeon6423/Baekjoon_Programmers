# width, height를 비교해서 둘 중 큰 값을 한 리스트에 넣고 나머지를 리스트로 
# 두 개의 리스트 중 가장 큰 값을 뽑아서 곱함
# 1. width,height를 리스트 생성
# 2. for문 돌면서 width,height를 중 큰 값은 width 리스트로 작은 값은 h리스트로
# 3. 두 리스트에서 가장 큰 값을 곱한 값이 답
def solution(sizes):
    width = []
    height = []
    for size in sizes:
        width.append(max(size))
        height.append(min(size))
    answer = max(width) * max(height)
    return answer