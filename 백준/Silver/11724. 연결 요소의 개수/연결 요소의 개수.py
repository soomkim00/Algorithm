import sys

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)

    for _ in range(M):
        s, e = map(int, input().split())
        edges[s].append(e)
        edges[e].append(s)

    count = 0
    stack = []
    for i in range(1, N + 1):
        if visited[i]:
            continue
        count += 1

        stack.append(i)

        while stack:
            now = stack.pop()
            if visited[now]:
                continue
            visited[now] = 1

            for next in edges[now]:
                if not visited[next]:
                    stack.append(next)

    print(count)


if __name__ == "__main__":
    solve()
