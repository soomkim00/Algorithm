import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    if N == 1:
        print(1)
        return
    elif N == 2:
        print(2)
        return
    tile = [0] * (N + 1)
    tile[1] = 1
    tile[2] = 2
    for i in range(3, N+1):
        tile[i] = tile[i-1] + tile[i-2]
    print(tile[N] % 10007)


if __name__ == "__main__":
    solve()
