import sys

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    print(abs(N - M))


if __name__ == "__main__":
    solve()
