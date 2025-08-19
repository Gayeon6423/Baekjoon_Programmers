from collections import deque

def bfs(maps, visited):
    """
    BFS(너비 우선 탐색)로 격자형 지도에서 시작점 (0,0)부터
    도착점 (len(maps)-1, len(maps[0])-1)까지의 '최단 거리'를 계산합니다.

    매개변수
    - maps   : 2차원 리스트. 0은 벽/이동 불가, 1은 길/이동 가능을 의미.
               이 함수는 maps를 '거리 기록용'으로 덮어쓰며, 방문한 칸에
               시작점으로부터의 누적 거리를 저장합니다.
    - visited: 2차원 리스트(0/1). 해당 칸을 방문했는지 여부를 기록.

    반환값
    - 도착점까지 도달 가능하면 최단 거리(정수)
    - 도달 불가하면 -1
    """

    # 델타(이동 방향) 정의
    # drow: 행 변화량 (하, 우, 상, 좌) 순서
    drow = (1, 0, -1, 0)   # 하, 우, 상, 좌 (행 증가/감소)
    dcol = (0, 1, 0, -1)   # 하, 우, 상, 좌 (열 증가/감소)

    # BFS에 사용할 큐(덱). FIFO 구조로 좌표를 넣고 뺍니다.
    quque = deque()        # 원래 'queue'가 자연스러우나 원본 유지
    quque.append((0, 0))   # 시작점 (0,0)에서 탐색 시작

    # 큐가 빌 때까지(탐색할 노드가 없을 때까지) 반복
    while quque:
        # 현재 탐색할 좌표를 꺼냄
        row, col = quque.popleft()

        # 현재 칸에서 4방향(하/우/상/좌)으로 이웃 칸들을 확인
        for i in range(4):
            nrow = row + drow[i]  # 이웃 칸의 행
            ncol = col + dcol[i]  # 이웃 칸의 열
            # i=0이면 -> nrow=1, ncol=0 (아래로 한칸 이동)
            # i=1이면 -> nrow=1, ncol=1 (오른쪽으로 한칸 이동)

            # 1) 범위 체크: 격자 밖이면 스킵
            #    (음수 인덱스/범위 초과 접근을 막아 IndexError를 예방)
            if nrow < 0 or ncol < 0 or nrow > len(maps) - 1 or ncol > len(maps[0]) - 1:
                continue  # 현재 방향은 무시하고 다음 방향으로 진행(현재 반복문 무시, 다음 반복문 실행)

            # 2) 방문 가능 조건 체크
            #    - 아직 방문하지 않았고(visited[nrow][ncol] == 0)
            #    - 이동 가능한 칸이어야 함(maps[nrow][ncol]이 1 이상이어야 길)
            #      ※ 이 코드에서는 '길'이 처음엔 1이고, 방문 시 '거리'로 덮어씌움
            if not visited[nrow][ncol] and maps[nrow][ncol]:
                # 방문 표시(다시 큐에 들어오지 않게 함)
                visited[nrow][ncol] = 1

                # 거리 갱신:
                # 현재 칸(row,col)의 거리 + 1을 다음 칸에 기록
                # 시작점 maps[0][0]은 보통 1로 주어지므로
                # 첫 방문 시 maps[nrow][ncol]은 2, 3, ...처럼 누적됩니다.
                maps[nrow][ncol] = maps[row][col] + 1

                # 다음 탐색 대상으로 큐에 추가
                quque.append((nrow, ncol))

    # BFS 종료 후 도착점의 값이 여전히 1이라면,
    # 시작점에서 한 번도 거리 갱신이 안 됐다는 뜻 -> 도달 불가
    if maps[len(maps) - 1][len(maps[0]) - 1] == 1:
        return -1

    # 도착점에 기록된 값(시작점으로부터의 최단 거리)을 반환
    return maps[len(maps) - 1][len(maps[0]) - 1]


def solution(maps):
    """
    외부에서 호출하는 래퍼 함수.
    - visited 배열을 생성/초기화하고
    - 시작점(0,0)을 방문 처리한 뒤
    - bfs를 호출하여 결과를 반환합니다.
    """

    # maps가 그래프 역할을 하며, 방문 여부는 별도로 visited에서 관리
    # visited는 maps와 같은 크기의 2차원 리스트(0:미방문, 1:방문)
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]

    # 시작점 방문 처리 (중복 방문 방지)
    visited[0][0] = 1

    # BFS 실행 결과(최단 거리 or -1) 반환
    return bfs(maps, visited)
