# 이중우선순위큐 : 최소힙과 최대힙을 지원하는 자료구조
import heapq

def solution(operations):
    answer = []
    quque = [] # 비어있는 큐 리스트 생성

    for operation in operations: # operations 반복
        x, num = operation.split()
        num = int(num)

        if x == "I": # 삽입 method
            heapq.heappush(quque, num) # heappush로 구현
        elif x == "D" and num == 1: # 최댓값 삭제 method
            if len(quque) != 0:
                max_val = max(quque)
                quque.remove(max_val) # 최댓값 구한 후 remove
        elif x == "D" and num == -1: # 최솟값 삭제 method
            if len(quque) != 0:
                heapq.heappop(quque) # heappop으로 구현

    if len(quque) == 0: # 큐가 비어있다면
        answer = [0,0]
    else: # 큐가 비어있지 않다면
        max_val = max(quque)
        min_val = heapq.heappop(quque)
        answer = [max_val, min_val]
    
    return answer