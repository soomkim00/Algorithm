import sys

sys.stdin = open("input.txt", "r")


def solve():
    T = int(input())

    for t in range(1, T + 1):
        N, K = map(int, input().split())
        field = [list(input()) for _ in range(N)]
        print(field)
        print(f"#{t} ")


if __name__ == "__main__":
    solve()

"""
#1 7
#2 19
"""