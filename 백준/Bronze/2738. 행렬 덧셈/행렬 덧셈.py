import sys

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    data1 = [list(map(int, input().split())) for _ in range(N)]
    data2 = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            print(data1[i][j] + data2[i][j], end=' ')
        print()


if __name__ == "__main__":
    solve()
