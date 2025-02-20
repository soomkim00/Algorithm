from collections import deque


def bfs(s, g, v):
    visited = [0] * (v + 1)
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        t = q.popleft()
        if t == g:  # 현재 지점이 도착지점인가?
            return visited[t] - 1   # 간선 개수 == 총 길이 -1
        for n in adj_list[t]:       # 인접 리스르 사용. 해당 노드에 인접한 노드들
            if visited[n] == 0:
                q.append(n)
                visited[n] = visited[t] + 1
    return 0


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]  # 인접 리스트, 노드 1번부터 -> V+1개

    # 인접 리스트 생성
    for _ in range(E):
        i, j = map(int, input().split())
        adj_list[i].append(j)
        adj_list[j].append(i)   # 방향이 없어서!

    S, G = map(int, input().split())
    result = bfs(S, G, V)
    print(f"#{tc} {result}")
