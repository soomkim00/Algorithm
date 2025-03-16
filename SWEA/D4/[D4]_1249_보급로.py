# 다익스트라: 거리 가중치가 있는 최단거리 탐색
# 2차원 배열의 경우
# 1 시작 칸 거리 0, 나머지 큰 값(inf) 설정. 시작 칸 방문
# 2 방문 칸 인접 칸 거리 계산
# 2-1 거리 = min(현재 칸까지 거리 + 인접 칸 코스트, 인접 칸 거리)
# 3 방문 안한 칸 중 거리가 가장 짧은 칸 방문
# 4 2~3 반복하다가 도착칸 방문시
# 5 도착 칸 거리가 인접 칸 거리보다 작으면. 최단거리 찾음!

def dijkstra(r, c, g_r, g_c):
    while True:
        # 현재 칸 방문 표시
        # 인접 칸 거리 계산
        visited[r][c] = 1
        cal_adj(r, c)
        # 현재 위치가 목표 지점이면
        # 그 위치의 거리 값이 인접 칸들의 거리값중 가장 작은지 검사
        if r == g_r and c == g_c:
            if is_real_goal(r, c):
                return dist[r][c]

        r, c = sel_pos()


# 델타 사용 인접 칸 거리를 최신화.
# min(현재 칸 거리+인접 칸 코스트, 인접 칸 거리)
def cal_adj(r, c):
    global n
    for dr, dc in delta:
        if 0 <= r + dr < n and 0 <= c + dc < n and visited[r + dr][c + dc] == 0:
            dist[r + dr][c + dc] = min(dist[r + dr][c + dc], dist[r][c] + cost[r + dr][c + dc])


# 델타 사용 인접 칸 거리값들과 비교
def is_real_goal(r, c):
    global n
    for dr, dc in delta:
        if 0 <= r + dr < n and 0 <= c + dc < n and dist[r][c] > dist[r + dr][c + dc]:
            return 0
    return 1


# 다음 이동할 칸 결정. 방문 안 한 칸 중 거리 값 최소인 칸 return
def sel_pos():
    min_dist = float('inf')
    nr, nc = 0, 0
    for r in range(n):
        for c in range(n):
            if visited[r][c] == 0 and dist[r][c] < min_dist:
                min_dist = dist[r][c]
                nr, nc = r, c
    return nr, nc


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    # 각 칸 코스트(공사시간), 해당 칸 까지의 거리, 방문여부 확인 리스트
    # 시작 칸 거리 0, 나머지 칸 무한대(inf)
    cost = [list(map(int, input())) for _ in range(n)]
    dist = [[float('inf')] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    dist[0][0] = 0

    # 시작 칸과 도착 칸 정보 설정
    # 인접 칸 탐색을 위한 상하좌우 델타
    # 시작,끝 좌표를 사용한 다익스트라 호출
    start_r, start_c, goal_r, goal_c = 0, 0, n - 1, n - 1
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = dijkstra(start_r, start_c, goal_r, goal_c)

    print(f'#{tc} {result}')
