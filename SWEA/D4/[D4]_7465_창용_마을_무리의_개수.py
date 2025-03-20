import sys

sys.stdin = open("input.txt", "r")


def find_king(x):
    if x == parents[x]:
        return x

    parents[x] = find_king(parents[x])
    return parents[x]


def union(x, y):
    king_x = find_king(x)
    king_y = find_king(y)

    if king_x == king_y:
        return

    if king_x > king_y:
        parents[king_y] = king_x
    else:
        parents[king_x] = king_y


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        adj_li = []
        for _ in range(M):
            s, e = map(int, input().split())
            adj_li.append((s, e))
            # adj_li.append((e, s))

        parents = [i for i in range(N + 1)]  # make_set()

        for s, e in adj_li:
            if find_king(s) != find_king(e):
                union(s, e)
        for i in range(1, N + 1):
            find_king(i)
        result = len(set(parents[1:]))

        print(f"#{tc} {result}")
