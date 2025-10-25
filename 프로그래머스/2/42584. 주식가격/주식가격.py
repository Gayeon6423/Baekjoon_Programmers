from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        time = 0
        price = prices.popleft()
        for p in prices:
            time += 1
            if price > p:
                break
        answer.append(time)
    return answer

from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        time = 0
        price = prices.popleft()
        for p in prices:
            time += 1
            if price > p:
                break
        answer.append(time)
    return answer