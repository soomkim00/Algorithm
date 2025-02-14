def dijkstra(r, c, g_r, g_c):
    visited[r][c] = 1
    cal_adj(r, c)


def cal_adj(r, c):
    global n
    for dr, dc in delta:
        if 0 <= r + dr < n and 0 <= c + dc < n and visited[r + dr][c + dc] == 0:
            dist[r + dr][c + dc] = min(dist[r + dr][c + dc], dist[r][c] + cost[r + dr][c + dc])


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    cost = [list(map(int, input())) for _ in range(n)]
    dist = [[float('inf')] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    dist[0][0] = 0

    start_r, start_c, goal_r, goal_c = 0, 0, n - 1, n - 1
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dijkstra(start_r, start_c, goal_r, goal_c)

    print(f'#{tc} ')
