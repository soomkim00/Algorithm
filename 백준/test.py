import sys
from collections import deque

input = sys.stdin.readline

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))


def solve():
    N = int(input())
    data = [list(map(int, input().strip())) for _ in range(N)]
    counts = []

    def bfs(sr, sc):
        q = deque()
        q.append((sr, sc))
        data[sr][sc] = 0
        count = 0
        while q:
            tr, tc = q.popleft()
            count += 1
            for dr, dc in delta:
                nr, nc = tr + dr, tc + dc
                if 0 <= nr < N and 0 <= nc < N and data[nr][nc]:
                    data[nr][nc] = 0
                    q.append((nr, nc))
        counts.append(count)

    for r in range(N):
        for c in range(N):
            if data[r][c]:
                bfs(r, c)

    counts.sort()
    print(len(counts))
    for cnt in counts:
        print(cnt)


if __name__ == '__main__':
    solve()
