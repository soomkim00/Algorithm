import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    stairs = [0] + [int(input()) for _ in range(N)]

    # N이 0인 경우
    if N == 0:
        print(0)
        return

    # dp[i][0]: i번째 계단을 "한 칸 전진"으로 밟았을 때의 최대 점수
    # dp[i][1]: i번째 계단을 "두 칸 전진 후 한 칸" 연속 2번째로 밟았을 때의 최대 점수
    dp = [[0, 0] for _ in range(N+1)]

    # 초기값 설정
    dp[1][0] = stairs[1]
    if N >= 2:
        dp[2][0] = stairs[2]             # 0→2 (두 칸 점프)
        dp[2][1] = stairs[1] + stairs[2] # 0→1→2 (한 칸 + 한 칸)

    # 점화식
    for i in range(3, N+1):
        # i를 두 칸 전진(i-2→i)으로 밟았을 때, 직전이 1칸이든 2칸이든 상관 없음
        dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + stairs[i]

        # i-1→i로 한 칸 전진해서 밟을 경우, 이전엔 반드시 두 칸 전진이어야(cnt reset) 연속 1칸이 두 번 이하
        dp[i][1] = dp[i-1][0] + stairs[i]

    # 마지막 계단(N)을 밟고 끝낼 수 있는 두 가지 경우 중 최대값
    print(max(dp[N][0], dp[N][1]))


if __name__ == "__main__":
    solve()
