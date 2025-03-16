# 땅 -> 물 거리 탐색하면 땅 * 필드 수 만큼의 반복 발생
# 물을 큐에 다 넣고 다중 출발 bfs로 최단거리를 구하면
# 필드 수 만큼만 반복이 발생!


from collections import deque

T = int(input())
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for t in range(1, T + 1):
    N, M = map(int, input().split())
    land = [list(input()) for _ in range(N)]

    # 물 좌표들 q에 추가
    # 물 좌표들 visited를 1로 초기화
    # 마지막에 땅들의 좌표를 다 탐색해야 하므로 q2에 땅 좌표들도 보관
    q = deque()
    q2 = deque()
    visited = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if land[r][c] == 'W':
                q.append((r, c))
                visited[r][c] = 1
            else:
                q2.append((r, c))

    # 물 좌표들을 기준으로 최단거리 탐색 bfs
    # 각 땅들의 visited == 해당 땅에서 가장 가까운 물까지의 최단거리 + 1(물을 1로 설정)
    while q:
        tr, tc = q.popleft()
        for dr, dc in delta:
            nr, nc = tr + dr, tc + dc
            if 0 <= nr < N and 0 <= nc < M and not(visited[nr][nc]):
                q.append((nr, nc))
                visited[nr][nc] = visited[tr][tc] + 1

    # 각 땅들의 visited 값의 합을 구하고 출력
    # 최단거리 == visited[땅] - 1
    result = 0
    for r, c in q2:
        result += visited[r][c] - 1

    print(f"#{t} {result}")
