import sys

sys.stdin = open("input.txt", "r")


def solve():
    T = int(input())

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        result = float('inf')

        if tc != 1:
            continue

        def cal(now, cnt):
            nonlocal result
            if now > 1000000:
                return
            if cnt >= M // N:
                return
            if now == M:
                result = cnt
                return

            if now < M:
                cal(now * 2, cnt + 1)
                cal(now + 1, cnt + 1)
            else:
                cal(now - 10, cnt + 1)
                cal(now - 1, cnt + 1)

        cal(N, 0)

        print(f"#{tc} {result}")


if __name__ == "__main__":
    solve()
