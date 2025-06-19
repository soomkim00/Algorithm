import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def solve():
    N, M, B = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(data)


if __name__ == '__main__':
    solve()
