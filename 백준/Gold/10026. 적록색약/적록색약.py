import sys
from collections import deque

input = sys.stdin.readline

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))


def solve():
    N = int(input())
    data = [list(input().strip()) for _ in range(N)]

    cnt1 = cnt2 = 0

    def bfs(r: int, c: int, colors: set):
        q = deque()
        q.append((r, c))
        visited[r][c] = True

        while q:
            tr, tc = q.popleft()

            for dr, dc in delta:
                nr, nc = tr + dr, tc + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and data[nr][nc] in colors:
                    q.append((nr, nc))
                    visited[nr][nc] = True

    # 일반 사용자 탐색
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                bfs(r, c, set(data[r][c]))
                cnt1 += 1

    # 색약 사용자 탐색
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                if data[r][c] in ('R', 'G'):
                    bfs(r, c, {'R', 'G'})
                else:
                    bfs(r, c, data[r][c])
                cnt2 += 1

    print(cnt1, cnt2)


if __name__ == '__main__':
    solve()
