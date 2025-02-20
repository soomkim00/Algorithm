# 큐를 사용한 bfs
# 수행시간 최적화 시도..!

from collections import deque


def bfs_maze(r, c, gr, gc):
    visited = [[0] * SIZE for _ in range(SIZE)]
    q = deque()
    visited[r][c] = 1
    q.append((r, c))
    while q:
        tr, tc = q.popleft()
        for dr, dc in delta:
            nr, nc = tr + dr, tc + dc
            if 0 <= nr < SIZE and 0 <= nc < SIZE and maze[nr][nc] != 1 and not visited[nr][nc]:
                if nr == gr and nc == gc:
                    return 1
                q.append((nr, nc))
                visited[nr][nc] = 1

    return 0


SIZE = 16
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(SIZE)]

    sr = sc = gr = gc = 0

    for r in range(SIZE):
        for c in range(SIZE):
            if maze[r][c] == 2:
                sr, sc = r, c
            elif maze[r][c] == 3:
                gr, gc = r, c

    print(f"#{tc} {bfs_maze(sr, sc, gr, gc)}")