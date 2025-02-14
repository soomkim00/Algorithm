# dfs 순회하면서
# 방문 체크 할때마다 end값과 같은가? 같으면 return 1
# 순환을 끝냈다 == return 발생 안했다 -> 도착 못했다 -> return 0

def check_route(start, end):
    visited = [0] * SIZE
    stack = [0] * SIZE
    top = -1
    now = start
    while True:
        if visited[now] == 0:
            visited[now] = 1
            if now == end:
                return 1
        for child in adj_list[now]:
            if visited[child] == 0:
                top += 1
                stack[top] = now
                now = child
                break
        else:
            if top == -1:
                break
            top -= 1
            now = stack[top + 1]
    return 0


SIZE = 100

for _ in range(1, 11):
    tc, e = map(int, input().split())
    edges = list(map(int, input().split()))
    adj_list = [[] for _ in range(SIZE)]

    for i in range(0, 2 * e, 2):
        adj_list[edges[i]].append(edges[i + 1])

    result = check_route(0, 99)

    print(f"#{tc} {result}")
