# BFS 구현(큐 사용)
# index를 1씩 키우면서 1개는 +, 1개는 -해주며 deque에 append

from collections import deque
def solution(numbers,target):
    count = 0
    quque = deque()
    quque.append((0,0))
    while quque:
        index, cur_sum  = quque.popleft()
        
        if index == len(numbers):
            if cur_sum == target:
                count += 1
        else:
            cur_num = numbers[index]
            quque.append((index + 1, cur_sum + cur_num))
            quque.append((index + 1, cur_sum - cur_num))
    return count



# from collections import deque
# def solution(numbers,target):
#     cnt = 0
#     quque = deque()
#     quque.append((0,0))
#     while quque:
#         idx, cur_sum = quque.popleft()
#         if idx == len(numbers):
#             if cur_sum == target:
#                 cnt += 1
#         else:
#             cur_num = numbers[idx]
#             quque.append((idx+1, cur_num + cur_sum))
#             quque.append((idx+1, cur_num - cur_sum))
#     return cnt
