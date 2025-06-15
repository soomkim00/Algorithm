import sys

input = sys.stdin.readline


def solve():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        data = dict()
        for _ in range(n):
            a, b = input().split()
            if b in data:
                data[b] += 1
            else:
                data[b] = 2

        result = 1
        for num in data.values():
            result *= num

        print(result - 1)


if __name__ == '__main__':
    solve()
