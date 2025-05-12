import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    time = list(map(int, input().split()))
    time.sort()
    for i in range(1, N):
        time[i] += time[i-1]
    print(sum(time))


if __name__ == "__main__":
    solve()
