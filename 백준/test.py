import sys
from collections import deque
from collections import deque

input = sys.stdin.readline


def solve():
    N = int(input())
    K = int(input())
    computer = [[] for _ in range(N + 1)]

    for _ in range(K):
        s, e = map(int, input().split())
        computer[s].append(e)
        computer[e].append(s)

    q = deque()
    q.append(1)
    visited = [0] * (N + 1)
    count = 0
    while q:
        now = q.popleft()
        if visited[now]:
            continue
        visited[now] = 1
        count += 1

        for next in computer[now]:
            q.append(next)

    if count:
        print(count - 1)
    else:
        print(count)


if __name__ == "__main__":
    solve()
