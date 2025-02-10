T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    # 방향 지정 델타와 방향을 바꿔줄 인덱스스
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dn = 0

    # 현재 위치 인덱스 설정, 첫 위치 값 1 할당
    i = j = 0
    snail[i][j] = 1

    # 첫 값인 1 제외 2부터 N**2 값이 기록될 때까지
    for n in range(2, N**2 + 1):
        # 기존 방향 델타 값
        di, dj = dir[dn][0], dir[dn][1]

        # 기존 방향 다음 순서가 0이 아니거나, 범위를 벗어나는지 체크
        # 해당되면 방향 전환
        if i + di >= N or j + dj >= N or snail[i + di][j + dj] != 0:
            dn = (dn + 1) % 4
            di, dj = dir[dn][0], dir[dn][1]

        i, j = i + di, j + dj
        snail[i][j] = n

    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=" ")
        print()
