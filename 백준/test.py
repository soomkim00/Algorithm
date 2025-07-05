import sys
from collections import deque

input = sys.stdin.readline

delta = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))


def solve():
    M, N, H = map(int, input().split())
    data = []
    for _ in range(H):
        layer = [list(map(int, input().split())) for _ in range(N)]
        data.append(layer)

    q = deque()
    remain = 0
    for d in range(H):
        for r in range(N):
            for c in range(M):
                if data[d][r][c] == 1:
                    q.append((d, r, c, 0))
                elif data[d][r][c] == 0:
                    remain += 1

    if not remain:
        print(0)
        return

    def bfs():
        nonlocal remain
        while q:
            td, tr, tc, day = q.popleft()
            for dd, dr, dc in delta:
                nd, nr, nc = td + dd, tr + dr, tc + dc
                if 0 <= nd < H and 0 <= nr < N and 0 <= nc < M and not data[nd][nr][nc]:
                    data[nd][nr][nc] = 1
                    remain -= 1
                    if not remain:
                        return day + 1
                    q.append((nd, nr, nc, day + 1))
        return -1

    print(bfs())


if __name__ == '__main__':
    solve()
