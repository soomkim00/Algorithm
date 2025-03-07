import sys

sys.stdin = open("input.txt", "r")


def dfs(r, c):
    return 1


T = int(input())
delta = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

for t in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    route_len = set()
    # 각 지점에서 길이를 구해서
    for r in range(N):
        for c in range(N):
            route = []
            dfs(r, c)



    print(f"#{t} ")
