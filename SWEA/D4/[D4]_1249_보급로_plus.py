# queue를 사용한 bfs로 좀 더 간단하게 풀어보자! (다익스트라 응용?)
# 한 지점을 방문할 때마다 인접 지점들을 가져와서
# 인접 지점까지의 기존 계산된 거리보다 해당 지점 거리+인접 지점 cost가 작다면
# 인접 지점 거리를 최신화하고, 큐에 추가
#   1 기존 지점 거리 계산이 처음인 경우, dist 값은 'inf'라서 무조건 현재지점에서 접근하는 경로 값으로 저장
#   2 다른 경로로 거리값이 이미 있는 경우, 비교를 통해 가장 짧은 경로의 거리값만 남김
# q가 비었으면 모든 경로를 탐색한 경우
# 이후 목표지점의 dist를 출력

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    q = deque()  # bfs를 위한 큐
    dist = [[float('inf')] * N for _ in range(N)]  # 거리 값은 비교를 위해 inf로 초기화
    cost = [list(map(int, input())) for _ in range(N)]  # 각 칸 cost 값 저장

    goal_r, goal_c = N - 1, N - 1  # 목표 지점
    now_r, now_c = 0, 0  # 시작점
    q.append((now_r, now_c))  # 큐에 시작점 추가
    dist[now_r][now_c] = 0  # 시작점 거리 정보 0
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 인접 지점 탐색을 위한 델타

    while q:
        # 큐에서 하나를 꺼내서 저장
        next_r, next_c = q.popleft()
    
        # 꺼낸 지점 인접 지점 탐색, 범위 안에 있는 지점에 대해
        # 거리 값 갱신 후 큐에 넣음
        for d_r, d_c in delta:
            n_r, n_c = next_r + d_r, next_c + d_c
            if 0 <= n_r < N and 0 <= n_c < N:
                if dist[n_r][n_c] > (dist[next_r][next_c] + cost[n_r][n_c]):
                    dist[n_r][n_c] = dist[next_r][next_c] + cost[n_r][n_c]
                    q.append((n_r, n_c))

    print(f'#{tc} {dist[goal_r][goal_c]}')