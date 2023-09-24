# BFS 구현(큐 사용)
# index를 1씩 키우면서 1개는 +, 1개는 -해주며 deque에 append
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