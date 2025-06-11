import sys

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))

    trees.sort(reverse=True)

    s = trees[0] - 1
    e = 0

    while s >= e:
        H = (s + e) // 2
        total = 0
        flag = 0

        for tree in trees:
            if H >= tree:
                break

            total += tree - H

            if total >= M:
                flag = 1
                break
        if flag:  # 현재 H가 충분히 낮다 -> 높여보자
            e = H + 1
        else:
            s = H - 1

    print(s)


if __name__ == "__main__":
    solve()
