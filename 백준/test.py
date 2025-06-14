import sys
from collections import deque

input = sys.stdin.readline

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 상 하 좌 우


def solve():
    M, N = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    q = deque()
    remain = 0

    for r in range(N):
        for c in range(M):
            if data[r][c] == 1:
                q.append((r, c, 0))
            elif data[r][c] == 0:
                remain += 1

    while q:
        tr, tc, day = q.popleft()

        if remain == 0:
            print(day)
            return

        for dr, dc in delta:
            nr, nc = tr + dr, tc + dc
            if 0 <= nr < N and 0 <= nc < M and data[nr][nc] == 0:
                data[nr][nc] = 1  # ← 여기서 반드시 표시해 줍니다
                remain -= 1
                if remain == 0:  # ← 마지막 토마토가 익은 즉시
                    print(day + 1)  # day+1 을 출력하고
                    return
                q.append((nr, nc, day + 1))

    print(-1)


if __name__ == '__main__':
    solve()
