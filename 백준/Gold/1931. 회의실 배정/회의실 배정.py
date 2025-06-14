import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    data = []
    for _ in range(N):
        s, e = map(int, input().split())
        data.append((s, e))

    data.sort(key=lambda x: x[0])
    data.sort(key=lambda x: x[1])

    time = 0
    cnt = 0

    for room in data:
        if room[0] < time:
            continue

        cnt += 1
        time = room[1]

    print(cnt)


if __name__ == '__main__':
    solve()
