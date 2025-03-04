# 각 노드의 자식 노드를 저장하는 2차원 배열을 선언해 저장
#   정점의 개수 = 간선 개수 + 1 (인덱스 0부터 시작해서 + 1)
# 저장된 트리의 시작점이 주어졌을 때. 해당 정점부터 서브트리틑 탐색
# dfs 혹은 bfs를 사용해서 전체 방문하면서 cnt 증가

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    edges = [[0] * (E + 2) for _ in range(2)]

    for i in range(0, 2 * E, 2):
        if edges[0][arr[i]] == 0:
            edges[0][arr[i]] = arr[i + 1]
        else:
            edges[1][arr[i]] = arr[i + 1]

    # 1. dfs
    cnt = 0
    stack = []
    visited = [0] * (E + 2)
    while True:
        if visited[N] == 0:
            cnt += 1
            visited[N] = 1
        for child in [edges[0][N], edges[1][N]]:
            if child and not visited[child]:
                stack.append(N)
                N = child
                break
        else:
            if stack:
                N = stack.pop()
            else:
                break

    # 2. bfs
    # cnt = 0
    # q = []
    # visited = [0] * (E + 2)
    # q.append(N)
    # while q:
    #     t = q.pop(0)
    #     cnt += 1
    #     for child in [edges[0][t], edges[1][t]]:
    #         if child and not visited[child]:
    #             q.append(child)
    #             visited[child] = 1

    print(f"#{tc} {cnt}")
