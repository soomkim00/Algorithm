T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    kill_count = []
    for i in range(N):
        for j in range(N):
            kill = 0
            for ni in range(i, i + M):
                for nj in range(j, j + M):
                    if 0 <= ni < N and 0 <= nj < N:
                        kill += flies[ni][nj]
            kill_count.append(kill)

    print(f'#{tc} {max(kill_count)}')
