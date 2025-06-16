import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    if n == 1:
        print(1)
        return
    elif n == 2:
        print(3)
        return
    dp = [0] * (n+1)

    dp[1] = 1
    dp[2] = 3

    for i in range(3, n+1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]

    print(dp[n] % 10007)


if __name__ == '__main__':
    solve()
