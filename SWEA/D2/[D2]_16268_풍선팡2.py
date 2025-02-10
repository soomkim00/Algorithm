# 상하좌우 이동 델타 설정
# 한 칸 기준에서 델타만큼 이동한 칸들 중
# 표를 넘어가지 않는 조건에서
# 모두 더한 합들 중 최댓값 출력

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    sum_set = []
    for i in range(N):
        for j in range(M):
            temp = 0
            temp += balloons[i][j]
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    temp += balloons[ni][nj]
            sum_set.append(temp)

    print(f"#{tc} {max(sum_set)}")
