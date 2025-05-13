import sys

input = sys.stdin.readline


def solve():
    T = int(input())
    memo = {0: (1, 0), 1: (0, 1)}

    def fibo_count(n):
        if n in memo:
            return memo[n]
        a0, a1 = fibo_count(n - 1)
        b0, b1 = fibo_count(n - 2)
        memo[n] = (a0 + b0, a1 + b1)
        return memo[n]

    for _ in range(T):
        n = int(input())
        c0, c1 = fibo_count(n)
        print(c0, c1)


if __name__ == "__main__":
    solve()
