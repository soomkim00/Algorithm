# 큐를 사용한 bfs
# 경로가 있는가?만 탐색하면 되기에 visited를 0,1로만 구성

from collections import deque


def bfs_maze(r, c):
    visited = [[0] * SIZE for _ in range(SIZE)]
    q = deque()
    visited[r][c] = 1
    q.append((r, c))
    while q:
        tr, tc = q.popleft()
        if maze[tr][tc] == 3:
            return 1
        for dr, dc in delta:
            nr, nc = tr + dr, tc + dc
            if 0 <= nr < SIZE and 0 <= nc < SIZE and maze[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1

    return 0


SIZE = 16
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(SIZE)]

    sr = sc = 0

    for r in range(SIZE):
        for c in range(SIZE):
            if maze[r][c] == 2:
                sr, sc = r, c

    print(f"#{tc} {bfs_maze(sr, sc)}")

"""
# dfs로 풀어보자!
# 파이참에선 돌아가는데.. SWEA에선 Memory Limit Exceeded가 뜬다ㅠㅠ

def dfs_maze(r, c):
    visited[r][c] = 1
    while True:
        if maze[r][c] == 3:
            return 1
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < SIZE and 0 <= nc < SIZE and not maze[nr][nc]:
                stack.append([r, c])
                visited[nr][nc] = 1
                r, c = nr, nc
                break
        else:
            if not stack:
                r, c = stack.pop()
            else:
                break
    return 0


SIZE = 16
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(SIZE)]
    visited = [[0] * SIZE for _ in range(SIZE)]
    stack = []
    sr = sc = 0

    for r in range(SIZE):
        for c in range(SIZE):
            if maze[r][c] == 2:
                sr, sc = r, c

    print(f"#{tc} {dfs_maze(sr, sc)}")
"""