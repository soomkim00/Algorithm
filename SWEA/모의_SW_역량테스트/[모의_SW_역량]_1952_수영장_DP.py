T = int(input())

for tc in range(1, T + 1):
    d, m, m3, y = map(int, input().split())
    use = [0] + list(map(int, input().split()))

    dp = [0] * 13
    dp[1] = min(m, use[1] * d)
    dp[2] = dp[1] + min(m, use[2] * d)
    for i in range(3, 13):
        dp[i] = min(dp[i - 1] + use[i] * d,
                    dp[i - 1] + m,
                    dp[i - 3] + m3)

    print(f"#{tc} {min(dp[12], y)}")
