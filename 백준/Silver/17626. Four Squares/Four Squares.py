import sys
import math
from collections import deque

input = sys.stdin.readline


def solve():
    n = int(input())

    # bfs
    q = deque()
    q.append((n, 0))  # 남은 수, 사용한(뺀) 제곱근 숫자

    while q:
        now, cnt = q.popleft()
        div = math.floor(math.sqrt(now))

        for i in range(div, 0, -1):
            remain = now - i ** 2
            if remain == 0:
                print(cnt + 1)
                return
            q.append((remain, cnt + 1))


if __name__ == '__main__':
    solve()
