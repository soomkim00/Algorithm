import sys

# sys.stdin = open("sample_input.txt", "r")


def dfs(graph, node, parents):
    for p in parents[node - 1]:
        if p not in visited:
            dfs(graph, p, parents)
    else:
        if node not in visited:
            visited.append(node)
        for next in graph[node - 1]:
            dfs(graph, next, parents)


for tc in range(1, 11):
    v, e = map(int, input().split())
    edges = list(map(int, input().split()))
    graph = [[] for _ in range(v)]
    parents = [[] for _ in range(v)]
    start_list = [0] * v

    for i in range(0, 2 * e, 2):
        graph[edges[i] - 1].append(edges[i + 1])
        parents[edges[i + 1] - 1].append(edges[i])
        start_list[edges[i + 1] - 1] += 1

    start = start_list.index(0) + 1
    visited = []
    dfs(graph, start, parents)

    print(f"#{tc}", *visited)
