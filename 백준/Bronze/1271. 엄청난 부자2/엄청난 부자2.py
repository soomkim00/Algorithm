import sys

input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())
    print(n // m)
    print(n % m)


if __name__ == '__main__':
    solve()
