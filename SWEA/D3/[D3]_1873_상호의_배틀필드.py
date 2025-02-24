T = int(input())

# 인덱스를 서로 맞추고, .index() 메서드를 적절히 활용해서
# 해당 커맨드에 맞는 델타와 전차 상태를 변경!
#           상       하       좌       우
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dir_li = ['^', 'v', '<', '>']
cmd_li = ['U', 'D', 'L', 'R']

for tc in range(1, T + 1):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]
    N = int(input())
    command = list(input())

    # 현재 위치와 초기화
    nr, nc = 0, 0
    for r in range(H):
        for c in range(W):
            if board[r][c] in dir_li:
                nr, nc = r, c

    # Game Start!
    for c in command:
        # print('!  ', c) : 디버깅용. 해당 커맨드가 뭐였는지 표시! 아래쪽 출력문과 함께 사용
        # 슛이면
        # 전차는 그대로, 포탄만 움직여야 하니까 포탄 인덱스 따로 저장하고
        # .index()를 사용해서 전차가 바라보고 있는 방향의 델타를 가져옴.
        # 범위 안에서 / 벽돌벽은 부수고 끝 / 강철 벽은 그냥 끝
        if c == "S":
            dr, dc = delta[dir_li.index(board[nr][nc])]
            br, bc = nr + dr, nc + dc
            while 0 <= br < H and 0 <= bc < W:
                if board[br][bc] == '*':
                    board[br][bc] = '.'
                    break
                elif board[br][bc] == '#':
                    break
                br += dr
                bc += dc

        # 방향이면
        # 일단 해당 방향으로 전차 상태 변환
        # 해당 방향 델타로 범위검사, 벽/물 검사 후 전진여부 결정
        # 못가면 다시 백스탭
        else:
            board[nr][nc] = dir_li[cmd_li.index(c)]
            dr, dc = delta[dir_li.index(board[nr][nc])]
            nr, nc = nr + dr, nc + dc
            if 0 <= nr < H and 0 <= nc < W and board[nr][nc] == '.':
                board[nr][nc], board[nr - dr][nc - dc] = board[nr - dr][nc - dc], board[nr][nc]
            else:
                nr, nc = nr - dr, nc - dc

        # 디버깅을 위한 출력문(실제 사용했던)
        # 매 커맨드를 실행할때마다 게임판의 상태 확인!
        # for r in range(H):
        #     for c in range(W):
        #         print(board[r][c], end='')
        #     print()
        # print('--------------')

    # 결과 출력
    print(f"#{tc} ", end='')
    for r in range(H):
        for c in range(W):
            print(board[r][c], end='')
        print()
