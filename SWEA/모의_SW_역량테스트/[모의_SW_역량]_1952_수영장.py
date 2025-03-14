import sys

sys.stdin = open("input.txt", "r")


# 총 금액 -> 가능한가?

def recur(month, temp):
    global min_cost

    # 최소값보다 현재값이 커지면 탐색 x
    if temp > min_cost:
        return

    # 1년 끝나면 결과 비교 후 최신화
    if month > 12:
        min_cost = min(min_cost, temp)
        return

    recur(month + 1, temp + use[month] * d)
    recur(month + 1, temp + m)
    recur(month + 3, temp + m3)
    recur(month + 12, temp + y)


T = int(input())

for tc in range(1, T + 1):
    d, m, m3, y = map(int, input().split())
    use = [0] + list(map(int, input().split()))

    min_cost = y
    recur(1, 0)

    print(f"#{tc} {min_cost}")
