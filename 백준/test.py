import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    num = list(int(input()) for _ in range(N))
    num.sort()
    print(round(sum(num)/N))
    print(num[N//2])
    print()
    print(num[-1] - num[0])


if __name__ == "__main__":
    solve()
