# 인접 리스트로 저장
# dfs로 탐색하면서, 방문시마다 같은지 검사, 같으면 1 return
# 탐색 끝났는데 return 안됐으면 없다는 말, 0 retrun

def dfs(s, g):
    top = -1
    while True:
        if not visited[s]:
            visited[s] = True
            if s == g:
                return 1
        for child in graph[s]:
            if not visited[child]:
                top += 1
                stack[top] = s
                s = child
                break
        else:
            top -= 1
            s = stack[top + 1]
        if top == -1:
            break

    return 0


T = int(input())

for tc in range(1, T + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        i, j = map(int, input().split())
        graph[i].append(j)
    start, goal = map(int, input().split())

    visited = [False] * (v + 1)
    stack = [0] * v
    result = dfs(start, goal)

    print(f"#{tc} {result}")
