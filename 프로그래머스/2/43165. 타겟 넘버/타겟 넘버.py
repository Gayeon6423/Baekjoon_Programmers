# BFS 구현(큐 사용)
# index를 1씩 키우면서 1개는 +, 1개는 -해주며 deque에 append
# solution1
from collections import deque
def solution(numbers,target):
    count = 0
    quque = deque()
    quque.append((0,0))
    while quque:
        cur_sum, index = quque.popleft()
        
        if index == len(numbers):
            if cur_sum == target:
                count += 1
        else:
            cur_num = numbers[index]
            quque.append((cur_sum + cur_num,index + 1))
            quque.append((cur_sum - cur_num, index + 1))
    return count

# solution2
def solution(numbers, target):
    leaves = [0] # 모든 결과
    count = 0
    for num in numbers:
        temp = []
    # 자손 노드
        for leaf in leaves:
            temp.append(leaf+num) # 더하는 경우
            temp.append(leaf-num) # 빼는 경우
        leaves = temp
    # 모든 경우의 수 계산 후 target과 같은지 확인
    for leaf in leaves:
        if leaf == target:
            count += 1
    return count
