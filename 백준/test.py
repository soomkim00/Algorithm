import sys
from collections import deque

input = sys.stdin.readline

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))


def solve():
    N, M = map(int, input().split())
    data = [list(input().strip()) for _ in range(N)]

    # 시작점 탐색
    sr, sc = 0, 0

    def find_start():
        nonlocal sr, sc
        for r in range(N):
            for c in range(M):
                if data[r][c] == 'I':
                    sr, sc = r, c
                    return

    find_start()

    # bfs
    result = 0  # 만난 사람
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((sr, sc))

    while q:
        tr, tc = q.popleft()

        if visited[tr][tc]:
            continue

        visited[tr][tc] = 1

        if data[tr][tc] == 'P':
            result += 1

        for dr, dc in delta:
            nr, nc = tr + dr, tc + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and data[nr][nc] != 'X':
                q.append((nr, nc))

    if result:
        print(result)
    else:
        print('TT')


if __name__ == '__main__':
    solve()
