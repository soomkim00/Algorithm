import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def solve():
    N = int(input())
    heap = []

    for _ in range(N):
        x = int(input())
        if x:
            heappush(heap, -x)
        elif heap:
            print(-heappop(heap))
        else:
            print(0)


if __name__ == '__main__':
    solve()
