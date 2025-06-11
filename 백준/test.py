import sys
from collections import deque

input = sys.stdin.readline


def solve():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    q = deque()
    q.append((0, 0, N - 1, N - 1))
    count = [0, 0]

    while q:
        r1, c1, r2, c2 = q.popleft()
        s = data[r1][c1]

        flag = True
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if data[r][c] != s:
                    flag = False
                    break
            if not flag:
                break

        if flag:
            count[s] += 1
        else:
            mid_r = (r1 + r2) // 2
            mid_c = (c1 + c2) // 2
            q.append((r1, c1, mid_r, mid_c))
            q.append((r1, mid_c + 1, mid_r, c2))
            q.append((mid_r + 1, c1, r2, mid_c))
            q.append((mid_r + 1, mid_c + 1, r2, c2))

    print(count[0])
    print(count[1])


if __name__ == "__main__":
    solve()
