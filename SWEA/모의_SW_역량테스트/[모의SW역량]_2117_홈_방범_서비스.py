T = int(input())
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우

for t in range(1, T + 1):
    N, M = map(int, input().split())
    houses = [list(map(int, input().split())) for _ in range(N)]

    # 집 개수 구하기
    cnt_house = 0
    for r in range(N):
        for c in range(N):
            if houses[r][c] == 1:
                cnt_house += 1

    # 최대 집 개수, 범위 (범위 1일때 한 집은 무조건 가능)
    max_house = 1
    k = 2

    # 범위를 증가시키면서 탐색
    # 최대 수익(집 수 * M)이 범위 k 발생하는 cost보다 작은 동안
    while cnt_house * M >= k ** 2 + (k - 1) ** 2:
        # 범위에 해당하는 비용
        cost = k ** 2 + (k - 1) ** 2

        # 각 지점(r,c)에서 범위 k만큼 탐색
        # 시작점부터 거리가 k-1인 지점까리 bfs로 탐색하면서
        # 집의 개수를 temp_max로 카운트
        for r in range(N):
            for c in range(N):
                visited = [[0] * N for _ in range(N)]
                q = []
                temp_max = 0
                q.append((r, c))
                visited[r][c] = 1
                while q:
                    tr, tc = q.pop(0)
                    # 집인가?
                    if houses[tr][tc] == 1:
                        temp_max += 1

                    # 해당 지점까지의 거리가 k-1보다 작으면 인접 칸 중 방문 안한 곳 큐에 추가
                    # 추가할 때 거리+1을 하기 때문에 k-1까지 찾으려면 그보다 하나 작은 경우를 고려!
                    if visited[tr][tc] <= k-1:
                        for dr, dc in delta:
                            nr, nc = tr + dr, tc + dc
                            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                                q.append((nr, nc))
                                visited[nr][nc] = visited[tr][tc] + 1  # 누적 거리 계산

                # 범위 내의 집이 최대 집 개수보다 작으면 통과
                if temp_max <= max_house:
                    continue
                # 범위 내의 집에서 받을 수익이 지출보다 작으면 통과
                elif temp_max * M < cost:
                    continue
                # 아니면 max_house 갱신
                else:
                    max_house = temp_max

        # 만약 집 최대값이 전체 집 수와 같아지면 더 이상 비교 불필요
        if max_house == cnt_house:
            break
        # 범위 1 증가
        k += 1

    print(f"#{t} {max_house}")