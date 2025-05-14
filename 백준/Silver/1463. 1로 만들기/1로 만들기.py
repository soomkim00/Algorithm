import sys
from collections import deque

input = sys.stdin.readline


def solve():
    N = int(input())
    result = 0
    q = deque()
    q.append((N, 0))

    while True:
        number, count = q.popleft()
        if number == 1:
            result = count
            break

        if number % 3 == 0:
            q.append((number // 3, count + 1))
        if number % 2 == 0:
            q.append((number // 2, count + 1))
        q.append((number - 1, count + 1))

    print(result)


if __name__ == "__main__":
    solve()
