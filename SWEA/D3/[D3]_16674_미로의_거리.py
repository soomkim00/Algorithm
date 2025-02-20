from collections import deque

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(r, c, n):
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append([r, c])
    visited[r][c] = 1
    while q:
        tr, tc = q.popleft()
        if maze[tr][tc] == 3:
            return visited[tr][tc] - 2
        for dr, dc in delta:
            nr, nc = tr + dr, tc + dc
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and visited[nr][nc] == 0:
                q.append([nr, nc])
                visited[nr][nc] = visited[tr][tc] + 1
    return 0

def find_path():
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                return bfs(r, c, N)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    result = find_path()

    print(f"#{tc} {result}")
