import sys

input = sys.stdin.readline


def solve():
    T = int(input())

    def fibo_count(n):
        nonlocal cnt0, cnt1
        if n == 0:
            cnt0 += 1
            return 0
        elif n == 1:
            cnt1 += 1
            return 1
        else:
            return fibo_count(n - 1) + fibo_count(n - 2)

    for _ in range(T):
        n = int(input())
        cnt0, cnt1 = 0, 0
        fibo_count(n)
        sys.stdout.write(str(cnt0) + ' ' + str(cnt1) + '\nl')


if __name__ == "__main__":
    solve()
