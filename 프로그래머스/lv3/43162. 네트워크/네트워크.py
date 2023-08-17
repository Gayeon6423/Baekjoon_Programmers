def solution(n, computers):
    answer = 0  # 네트워크의 개수를 저장할 변수

    visited = [0 for i in range(len(computers))]  # 각 컴퓨터의 방문 여부를 저장하는 리스트

    def DFS(i):  # 깊이 우선 탐색 함수 정의
        visited[i] = 1  # 현재 컴퓨터를 방문처리
        for a in range(n):  # 모든 컴퓨터에 대해
            if computers[i][a] and not visited[a]:  # 연결되어 있고 방문하지 않은 컴퓨터면
                DFS(a)  # 해당 컴퓨터로 DFS 수행

    for i in range(n):  # 모든 컴퓨터에 대해
        if not visited[i]:  # 아직 방문하지 않은 컴퓨터면
            DFS(i)  # 해당 컴퓨터부터 DFS 수행
            answer += 1  # 네트워크 수 증가

    return answer  # 전체 네트워크 수 반환
