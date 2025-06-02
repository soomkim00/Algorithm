import sys

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    add_data = [0] * N
    add_data[0] = data[0]
    for i in range(1, N):
        add_data[i] = data[i] + add_data[i-1]

    for _ in range(M):
        i, j = map(int, input().split())
        idx_i, idx_j = i - 2, j - 1
        if idx_i == -1:
            print(add_data[idx_j])
        else:
            print(add_data[idx_j] - add_data[idx_i])


if __name__ == "__main__":
    solve()
