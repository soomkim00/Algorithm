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

    data = list(map(int, input().split()))

    result = 0
    first = data[0]
    second = 0
    idx = 1
    temp = 1

    for i in range(1, N):
        temp += 1
        if data[i] != first:
            second = data[i]
            result = temp
            idx = i + 1
            break

    if second == 0:
        print(temp)
        return

    s_temp = 1
    for i in range(idx, N):
        if data[i] != first and data[i] != second:
            first = second
            second = data[i]
            result = max(result, temp)
            temp = s_temp + 1
            s_temp = 1
        elif data[i] == first:
            first = second
            second = data[i]
            temp += 1
        elif data[i] == second:
            temp += 1
            s_temp += 1

    result = max(result, temp)

    print(result)


if __name__ == '__main__':
    solve()
