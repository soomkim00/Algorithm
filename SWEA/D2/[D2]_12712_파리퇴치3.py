T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    # + 용 델타, x 용 델타 따로 설정
    d_cross = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    d_diag = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    kill_list = []

    # 이중리스트 전체 순환하면서 각 지점에 대해
    for i in range(N):
        for j in range(N):
            kill = 0
            kill += flies[i][j]

            # + 방향으로 M 만큼 뻗어가면서 더함
            # 각 더해진 값이 범위를 벗어나는지 검사
            for a in range(1, M):
                for ci, cj in d_cross:
                    ni, nj = i + a * ci, j + a * cj
                    if 0 <= ni < N and 0 <= nj < N:
                        kill += flies[ni][nj]
            kill_list.append(kill)

            # x 방향도 동일하게 검사
            kill = 0
            kill += flies[i][j]
            for b in range(1, M):
                for di, dj in d_diag:
                    ni, nj = i + b * di, j + b * dj
                    if 0 <= ni < N and 0 <= nj < N:
                        kill += flies[ni][nj]
            kill_list.append(kill)

    print(f"#{tc} {max(kill_list)}")
