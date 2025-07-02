import sys
from collections import deque

input = sys.stdin.readline


def solve():
    N = int(input())
    adj_list = [list(map(int, input().split())) for _ in range(N)]

    result = [[0] * N for _ in range(N)]

    def bfs(s):
        q = deque()
        q.append(s)
        while q:
            now = q.popleft()
            for idx in range(N):
                if adj_list[now][idx] and not result[s][idx]:
                    result[s][idx] = 1
                    q.append(idx)

    for start in range(N):
        bfs(start)

    for r in result:
        print(*r)


if __name__ == '__main__':
    solve()
