import sys

input = sys.stdin.readline


def solve():
    data = set()
    for _ in range(28):
        data.add(int(input()))

    for i in range(1, 31):
        if i not in data:
            print(i)


if __name__ == "__main__":
    solve()
