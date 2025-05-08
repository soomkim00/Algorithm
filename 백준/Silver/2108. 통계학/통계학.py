import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    num = list(int(input()) for _ in range(N))
    num.sort()
    count = {}
    for n in num:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    max_count = max(count.values())
    max_num = []
    for n in count:
        if max_count == count[n]:
            max_num.append(n)

    result = 0
    if len(max_num) > 1:
        result = max_num[1]
    else:
        result = max_num[0]

    print(round(sum(num) / N))
    print(num[N // 2])
    print(result)
    print(num[-1] - num[0])


if __name__ == "__main__":
    solve()
