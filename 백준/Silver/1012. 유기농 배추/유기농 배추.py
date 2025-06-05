import sys
from collections import deque

input = sys.stdin.readline

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 상 하 좌 우


def solve():
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        board = [[0] * M for _ in range(N)]
        visited = [[0] * M for _ in range(N)]

        for _ in range(K):
            c, r = map(int, input().split())
            board[r][c] = 1

        def bfs(kr, kc):
            q = deque()
            q.append((kr, kc))
            while q:
                tr, tc = q.popleft()
                if visited[tr][tc]:
                    continue
                visited[tr][tc] = 1
                for dr, dc in delta:
                    nr, nc = tr + dr, tc + dc
                    if 0 <= nr < N and 0 <= nc < M and board[nr][nc]:
                        q.append((nr, nc))

        count = 0
        for r in range(N):
            for c in range(M):
                if not (visited[r][c]) and board[r][c]:
                    count += 1
                    bfs(r, c)

        print(count)


if __name__ == "__main__":
    solve()
