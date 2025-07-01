import sys

input = sys.stdin.readline


def solve():
    T = int(input())
    for _ in range(T):
        data = input().strip()
        print(data[0] + data[-1])


if __name__ == '__main__':
    solve()
