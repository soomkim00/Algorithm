import sys

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    data = {}

    for _ in range(N):
        key, val = input().split()
        data[key] = val

    for _ in range(M):
        print(data[input().rstrip()])


if __name__ == "__main__":
    solve()
