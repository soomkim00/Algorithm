import sys
from collections import deque

input = sys.stdin.readline

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))


def solve():
    N, M = map(int, input().split())
    data = [list(map(int, input().strip())) for _ in range(N)]

    q = deque()
    q.append((0, 0, 1))
    data[0][0] = 0
    while q:
        tr, tc, cnt = q.popleft()

        for dr, dc in delta:
            nr, nc = tr + dr, tc + dc

            if 0 <= nr < N and 0 <= nc < M and data[nr][nc]:
                if nr == N - 1 and nc == M - 1:
                    print(cnt + 1)
                    return
                data[nr][nc] = 0
                q.append((nr, nc, cnt + 1))


if __name__ == '__main__':
    solve()
