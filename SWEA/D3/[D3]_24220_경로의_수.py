import sys

sys.stdin = open("input.txt", "r")


def dfs(pos):
    global cnt
    if pos == G:
        cnt += 1
        return

    for next in graph[pos]:
        if visited[next] == 0:
            visited[next] = 1
            dfs(next)
            visited[next] = 0


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N, E = map(int, input().split())
        data = list(map(int, input().split()))
        S, G = map(int, input().split())

        graph = [[] for _ in range(N + 1)]
        for i in range(0, 2 * E, 2):
            graph[data[i]].append(data[i + 1])

        cnt = 0
        visited = [0] * (N + 1)
        dfs(S)

        print(f"#{tc} {cnt}")
