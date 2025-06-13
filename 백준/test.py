import sys
from heapq import heappop, heappush
from pprint import pprint

input = sys.stdin.readline

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 상 하 좌 우


def solve():
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    dist = [[float('inf')] * m for _ in range(n)]

    sr, sc = 0, 0

    for r in range(n):
        for c in range(m):
            if data[r][c] == 2:
                sr, sc = r, c
            elif data[r][c] == 0:
                dist[r][c] = 0

    dist[sr][sc] = 0

    h = []
    heappush(h, (0, sr, sc))

    while h:
        now_dist, tr, tc = heappop(h)

        if dist[tr][tc] < now_dist:
            continue

        for dr, dc in delta:
            nr, nc = tr + dr, tc + dc
            if 0 <= nr < n and 0 <= nc < m and data[nr][nc] and now_dist + 1 < dist[nr][nc]:
                dist[nr][nc] = now_dist + 1
                heappush(h, (now_dist + 1, nr, nc))

    for r in range(n):
        for c in range(m):
            if dist[r][c] == float('inf'):
                dist[r][c] = -1

    for r in range(n):
        print(*dist[r])


if __name__ == '__main__':
    solve()
