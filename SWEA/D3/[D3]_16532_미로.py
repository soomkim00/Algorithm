def is_route(s_r, s_c, n):
    stack = []
    visited = [[0] * n for _ in range(n)]

    n_r, n_c = s_r, s_c

    while True:

        print(n_r, n_c)
        print(visited)
        if maze[n_r][n_c] == 3:
            return 1

        stack.append((n_r, n_c))
        for dr, dc in delta:
            nr = n_r + dr
            nc = n_c + dc
            if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] != 1 and not visited[nr][nc]:
                stack.append((n_r, n_c))
                visited[nr][nc] = 1
                n_r, n_c = nr, nc
                break
        else:
            if stack:
                n_r, n_c = stack.pop()
            else:
                break
    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    start_r = start_c = goal_r = goal_c = 0

    #  시작점, 도착점 설정
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                start_r, start_c = r, c
            elif maze[r][c] == 3:
                goal_r, goal_c = r, c

    result = is_route(start_r, start_c, N)

    print(f"#{tc} {result}")
