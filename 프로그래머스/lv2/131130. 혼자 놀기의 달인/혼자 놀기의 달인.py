def solution(cards):
    answer = []  # 결과 값을 담을 리스트
    visited = [False] * (len(cards) + 1)  # 각 카드의 방문 여부를 저장하는 리스트

    for v in cards:
        if not visited[v]:
            tmp = []  # 현재 그룹의 카드들을 담을 임시 리스트
            while v not in tmp:
                tmp.append(v)
                v = cards[v - 1]  # 현재 카드의 연결된 다음 카드 인덱스
                visited[v] = True  # 현재 카드 방문 처리

            answer.append(len(tmp))  # 현재 그룹의 크기를 결과 리스트에 추가

    answer.sort(reverse=True)  # 그룹 크기를 내림차순으로 정렬

    if len(answer) >= 2:  # 그룹이 2개 이상일 때만
        return answer[0] * answer[1]  # 가장 큰 두 그룹의 크기를 곱한 결과 반환
    else:
        return 0  # 그룹이 2개 미만이면 결과는 0