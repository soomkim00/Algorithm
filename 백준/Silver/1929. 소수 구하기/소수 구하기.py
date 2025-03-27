import sys

input = sys.stdin.readline


def solve():
    M, N = map(int, input().split())
    jump = set()
    for i in range(2, N + 1):
        if i in jump:
            continue
        if M <= i <= N:
            print(i)
        mul = 1
        j = i
        while j <= N:
            j = i * mul
            jump.add(j)
            mul += 1


if __name__ == "__main__":
    solve()
