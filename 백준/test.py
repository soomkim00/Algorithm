import sys

input = sys.stdin.readline


def round(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


def solve():
    N = int(input())
    if N == 0:
        print(0)
    else:
        data = []
        for _ in range(N):
            data.append(int(input()))
        cut = round(N * 0.15)
        data.sort()
        cutted_data = data[cut:N - cut]
        print(round(sum(cutted_data) / (N - 2 * cut)))


if __name__ == "__main__":
    solve()
