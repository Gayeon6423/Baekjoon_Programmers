from collections import deque

def solution(n, vertex):
    # 1) 인접 리스트
    graph = [[] for _ in range(n + 1)]
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    # 2) 거리 배열 (-1은 미방문)
    dist = [-1] * (n + 1)
    dist[1] = 0

    # 3) BFS
    q = deque([1])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    # 4) 가장 먼 거리의 노드 개수
    max_d = max(dist)
    return dist.count(max_d)
