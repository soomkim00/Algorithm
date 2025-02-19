# B:1 / W:2
# 벽에 만나서 끝나는 조건을 어떻게 설정??

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 초기 판 상태 설정
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1], board[N // 2][N // 2] = 2, 2
    board[N // 2 - 1][N // 2], board[N // 2][N // 2 - 1] = 1, 1

    # 델타 (상/하/좌/우/상좌/상우/하좌/하우)
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
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] !=  0 and board[nr][nc] != board[r][c]:
                flag = True
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
