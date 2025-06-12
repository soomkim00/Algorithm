import sys
from collections import deque

input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    q = deque()
    memo = set()
    q.append((N, 0))

    while q:
        pos, cnt = q.popleft()

        # 종료조건
        if pos == K:
            print(cnt)
            return

        # 메모이제이션
        if pos in memo or pos < 0 or pos > 100000:
            continue
        memo.add(pos)

        q.append((pos - 1, cnt + 1))
        q.append((pos + 1, cnt + 1))
        q.append((pos * 2, cnt + 1))


if __name__ == '__main__':
    solve()
