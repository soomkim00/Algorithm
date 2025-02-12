# 이차원 배열 순환하면서
# 각 지점에 대한 8방향 값 접근
# 범위 이탈 확인 후
# 현재 지점의 값보다 작으면 check_heights += 1
# 8방향 검색 후 check_heights가 4보다 크면
# 후보지 개수인 cnd_cnt 1 증가

SIZE = 3
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    heights = [list(map(int, input().split())) for _ in range(N)]
    cnd_cnt = 0

    d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    for r in range(N):
        for c in range(M):
            check_heights = 0
            for dr, dc in d:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    if heights[nr][nc] < heights[r][c]:
                        check_heights += 1
            if check_heights >= 4:
                cnd_cnt += 1

    print(f"#{tc} {cnd_cnt}")
