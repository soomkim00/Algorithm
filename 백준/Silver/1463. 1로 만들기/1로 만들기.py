import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    dp = [0] * (N + 1)  # dp[i] = i를 1로 만드는 최소 연산 횟수

    for i in range(2, N + 1):
        # 1을 빼는 경우
        dp[i] = dp[i - 1] + 1

        # 2로 나누어 떨어질 때
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        # 3으로 나누어 떨어질 때
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    print(dp[N])

if __name__ == "__main__":
    solve()
