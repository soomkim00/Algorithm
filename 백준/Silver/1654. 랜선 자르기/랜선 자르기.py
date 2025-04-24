import sys

input = sys.stdin.readline


def solve():
    K, N = map(int, input().split())
    lines = [int(input()) for _ in range(K)]

    # 이진탐색
    l = 0
    r = max(lines)
    answer = 0
    while l <= r:
        mid = l + (r - l) // 2
        count = 0

        if mid == 0:
            answer = 1
            break

        for line in lines:
            count += line // mid
        if count >= N:
            answer = mid
            l = mid + 1
        else:
            r = mid - 1
    print(answer)
    return


if __name__ == "__main__":
    solve()
