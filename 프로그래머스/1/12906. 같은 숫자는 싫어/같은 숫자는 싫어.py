from collections import deque
def solution(arr):
    # 큐 생성
    answer = deque()
    for i,j in enumerate(arr):
        # 처음 나온 숫자라면
        if i == 0:
            answer.append(j)
        # 연속적인 숫자가 아니라면
        elif arr[i-1] != arr[i]:
            # 정답 리스트에 원소 추가
            answer.append(j)
        # 연속적인 숫자라면
        else:
            # 통과
            pass
    answer = list(answer)
    return answer