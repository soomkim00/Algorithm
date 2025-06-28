import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def solve():
    N = int(input())
    heap = []

    for _ in range(N):
        x = int(input())
        if x:
            heappush(heap, (abs(x), x))
        else:
            if heap:
                print(heappop(heap)[1])
            else:
                print(0)


if __name__ == '__main__':
    solve()
