import sys

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    data = [i for i in range(1, N + 1)]
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        data[i], data[j] = data[j], data[i]
    print(*data)


if __name__ == "__main__":
    solve()
