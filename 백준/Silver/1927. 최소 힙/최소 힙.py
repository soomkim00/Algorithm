import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def solve():
    N = int(input())
    data = []
    for _ in range(N):
        num = int(input())
        if num:
            heappush(data, num)
        elif data:
            print(heappop(data))
        else:
            print(0)


if __name__ == "__main__":
    solve()
