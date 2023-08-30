def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0

    while len(progresses) > 0:
        # 첫번째가 100이 될 때까지 loop를 돌며 time을 늘린다.
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        # 첫번째가 100이 안돼면 count 초기화    
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

progresses = [93, 30, 55]
speeds = [1,30,5]
solution(progresses, speeds)