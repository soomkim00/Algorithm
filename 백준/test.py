import sys

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    for i in range(1, N):
        data[i] += data[i-1]

    for _ in range(M):
        i, j = map(int, input().split())
        idx_i, idx_j = i - 2, j - 1
        if idx_i == -1:
            print(data[idx_j])
        else:
            print(data[idx_j] - data[idx_i])


if __name__ == "__main__":
    solve()
