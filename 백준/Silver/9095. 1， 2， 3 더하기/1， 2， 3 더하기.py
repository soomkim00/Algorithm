import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    for _ in range(N):
        number = int(input())
        count = 0

        def dfs(total):
            nonlocal count

            if total > number:
                return
            elif total == number:
                count += 1
                return

            for add_num in (1, 2, 3):
                dfs(total + add_num)

        dfs(0)
        print(count)


if __name__ == "__main__":
    solve()
