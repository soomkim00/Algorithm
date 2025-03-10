# bfs를 사용한 풀이
# 이 문제에선 그냥 인덱스 기반 접근해도 됩니다.(다른 제출) 참고용..!
# 그림과 같은 영역은 중앙점부터 상하좌우 델타 방향으로 N//2 길이 이하의 모든 지점이다
# 따라서 중앙점을 시작으로 N//2 길이만큼 bfs를 사용해 탐색하면서 값을 더해도 된다!

from collections import deque

T = int(input())
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우
for t in range(1, T + 1):
    N = int(input())
    value = [list(map(int, input())) for _ in range(N)]

    total = 0
    r = c = N // 2  # 중앙점 설정
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    total += value[r][c]
    while q:
        tr, tc = q.popleft()
        if visited[tr][tc] > N // 2:
            continue
        for dr, dc in delta:
            nr, nc = tr + dr, tc + dc
            if 0 <= nr < N and 0 <= nc < N and not (visited[nr][nc]):
                q.append((nr, nc))
                visited[nr][nc] = visited[tr][tc] + 1
                total += value[nr][nc]

    print(f"#{t} {total}")
