import sys

input = sys.stdin.readline


def solve():
    K, N = map(int, input().split())
    lines = [int(input()) for _ in range(K)]

    lenght = min(lines)
    cnt = 0
    while True:
        for line in lines:
            cnt += line // lenght
        if cnt >= N:
            break
        else:
            cnt = 0
            lenght //= 2

    # 그리디 -> 시간초과
    # while True:
    #     cnt = 0
    #     lenght += 1
    #     for line in lines:
    #         cnt += line // lenght
    #     if cnt < N:
    #         lenght -= 1
    #         break

    # 이진탐색

    l = lenght
    r = lenght * 2
    while l <= r:
        mid = l + (r - l) // 2
        cnt = 0
        for line in lines:
            cnt += line // mid
        if cnt


if __name__ == "__main__":
    solve()
