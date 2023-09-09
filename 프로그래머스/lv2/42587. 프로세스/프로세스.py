from collections import deque

def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    order = 0  # 실행된 프로세스 순서

    while queue:
        process, index = queue.popleft()  # 큐에서 프로세스 하나 꺼냄
        if any(process < p[0] for p in queue):  # 남은 프로세스 중 우선순위가 더 높은 것이 있는지 확인
            queue.append((process, index))  # 우선순위 높은 것 있다면 현재 프로세스 다시 큐에 넣음
        else:
            order += 1  # 순서 증가
            if location == index:  # 실행한 프로세스가 목표 프로세스이면
                return order