import sys

input = sys.stdin.readline


def solve():
    data = list(input().strip())
    miss_idx = 0
    total = 0

    for i in range(13):
        if not data[i].isdecimal():
            miss_idx = i
            continue

        if i % 2 == 0:
            total += int(data[i])
        else:
            total += 3 * int(data[i])

    ans = 0
    while True:
        if miss_idx % 2 == 0:
            add_num = ans
        else:
            add_num = 3 * ans

        if (total + add_num) % 10 == 0:
            print(ans)
            return
        ans += 1


if __name__ == '__main__':
    solve()
