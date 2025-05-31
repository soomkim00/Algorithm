import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    numbers = [int(input()) for _ in range(T)]
    max_n = max(numbers)

    dp = [0] * (max_n + 1)
    dp[0] = 1

    for i in range(1, max_n + 1):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        if i - 3 >= 0:
            dp[i] += dp[i - 3]

    for num in numbers:
        print(dp[num])

if __name__ == "__main__":
    solve()
