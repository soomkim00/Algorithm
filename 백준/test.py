import sys
from collections import deque

input = sys.stdin.readline


def solve():
    n, m, v = map(int, input().split())
    edges_d = [[] for _ in range(n + 1)]  # 노드 번호 1번부터, 0번 버림
    edges_b = [[] for _ in range(n + 1)]

    for _ in range(m):
        s, e = map(int, input().split())
        edges_d[s].append(e)
        edges_d[e].append(s)  # 양방향 그래프
        edges_b[s].append(e)
        edges_b[e].append(s)  # 양방향 그래프

    for edge_d in edges_d:
        edge_d.sort(reverse=True)

    for edge_b in edges_b:
        edge_b.sort()

    result_dfs = []
    result_bfs = []

    visited_dfs = set()
    visited_bfs = set()

    q = deque()
    stack = deque()

    q.append(v)
    stack.append(v)

    # dfs
    while stack:
        now = stack.pop()
        if now in visited_dfs:
            continue
        visited_dfs.add(now)
        result_dfs.append(now)
        for next in edges_d[now]:
            if next not in visited_dfs:
                stack.append(next)

    # bfs
    while q:
        now = q.popleft()
        if now in visited_bfs:
            continue
        visited_bfs.add(now)
        result_bfs.append(now)
        for next in edges_b[now]:
            if next not in visited_bfs:
                q.append(next)

    print(*result_dfs)
    print(*result_bfs)


if __name__ == '__main__':
    solve()
