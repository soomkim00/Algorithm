import sys

input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    coins = [int(input().rstrip()) for _ in range(N)]
    idx = len(coins) - 1
    count = 0

    while K:
        if coins[idx] <= K:
            temp = K // coins[idx]
            count += temp
            K -= temp * coins[idx]
        idx -= 1

    print(count)


if __name__ == "__main__":
    solve()
