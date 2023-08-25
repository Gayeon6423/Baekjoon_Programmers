from collections import deque
def solution(people, limit):
    count = 0                      # 구명보트 개수
    people = deque(sorted(people)) # 오름차순, 사람들의 몸무게 기준
    
    # 모든 사람이 구출될 때 까지
    while people:
        # 몸무게가 가장 큰 사람 구출
        person = people.pop()
        # 아직 남은사람이 있고, 가장 가벼운 사람이 무거운 사람과 같이타도 무게 제한에 안걸리면 같이 구출
        if len(people) > 0 and person + people[0] <= limit:
            people.popleft()
            
        count += 1
    
    return count