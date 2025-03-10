# B:1 / W:2
# 한 칸에 돌을 놓고 나면 델타 방향(8방향)으로 탐색하면서
# 다른 색 돌이 있는지 보고
# 있다면 해당 방향으로 탐색 진행하면서 지나가는 자리를 point_li에 저장
# 다시 같은 색 돌을 만나면 지나온 경로의 돌들의 색을 바꿈
# 빈 칸을 만나거나 벽을 만나면 탐색 중지(다음 탐색으로 넘어감)

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 초기 판 상태 설정
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1], board[N // 2][N // 2] = 2, 2
    board[N // 2 - 1][N // 2], board[N // 2][N // 2 - 1] = 1, 1

    # 델타 (상 / 하 / 좌 / 우 / 상좌 / 상우 / 하좌 / 하우)
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for _ in range(M):
        # 입력 좌표가 이쁘네^^ 0부터 시작하는 r,c로 변경
        c, r, st = map(int, input().split())
        r -= 1
        c -= 1
        board[r][c] = st
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            point_li = []
            if 0 <= nr < N and 0 <= nc < N and board[r][c] + board[nr][nc] == 3:
                while 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] == 0:
                        break
                    if board[nr][nc] == st:
                        for xr, xc in point_li:
                            board[xr][xc] = st
                        break
                    point_li.append((nr, nc))
                    nr += dr
                    nc += dc
        # 디버깅용 출력문. 돌을 놓을 때마다 게임판 상태 출력
        # for i in range(N):
        #     print(*board[i])
        # print()

    b_cnt = w_cnt = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                b_cnt += 1
            elif board[r][c] == 2:
                w_cnt += 1

    print(f"#{tc}", b_cnt, w_cnt)
