def solution(progresses, speeds):
    answer = []
    time = 0 # 날짜
    cnt = 0 # 배포 작업 수

    while len(progresses) > 0:
        # progresses 존재할 때까지 반복
        if (progresses[0] + speeds[0]*time) >= 100:
            # 첫번째 작업이 100이 되면 배포 작업 수인 cnt 증가
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            # 첫번째 작업이 100이 안돼면 time 증가, 기존 cnt는 answer에 추가 후 0으로 초기화
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            time += 1
    answer.append(cnt)
    return answer