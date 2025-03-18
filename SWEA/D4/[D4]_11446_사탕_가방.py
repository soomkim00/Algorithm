import sys

sys.stdin = open("input.txt", "r")


# 각 사탕을 몇개씩 넣어야.. -> 가방을 몇 개를 써야..!
# 가방의 개수는 하나씩 증가, 특정 값이 가능하면 그것보다 큰 값은 모두 가능..
# 즉 정렬된 상태처럼 사용 가능 -> 이진 탐색
# 적당히 큰 가방의 개수를 설정하고, 가방의 개수 기준으로 이진 탐색하며
# 각 가방의 개수가 가능한지를 체크
# 적당히 큰 값? 가장 많은 사탕의 개수


def solve():
    T = int(input())

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        data = list(map(int, input().split()))
        left = 1
        right = max(data)
        while left <= right:
            middle = left + (right - left) // 2
            # middle 개의 가방을 만들 수 있는가?
            # 각 사탕을 middle개로 나눠서 넣어서 총 합이 M이 넘는가?
            total = 0
            for d in data:
                total += d // middle
            if total < M:
                right = middle - 1
            else:
                left = middle + 1

        print(f"#{tc} {right}")


if __name__ == "__main__":
    solve()
