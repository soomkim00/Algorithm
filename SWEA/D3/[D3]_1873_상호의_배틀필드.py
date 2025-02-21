T = int(input())

#           상       하       좌       우
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dir_li = ['^', 'v', '<', '>']
cmd_li = ['U', 'D', 'L', 'R']

for tc in range(1, T + 1):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]
    N = int(input())
    command = list(input())

    # 현재 위치와, 방향 표시 인덱스 초기화
    dir = 0
    nr, nc = 0, 0
    for r in range(H):
        for c in range(W):
            if board[r][c] in dir_li:
                nr, nc = r, c
                dir = dir_li.index(board[r][c])

    # Game Start!
    for c in command:
        print('!  ', c)
        # 슛이면
        # 전차는 그대로, 포탄만 움직여야 하니까 포탄 인덱스 따로 저장하고
        # dir을 통해서 바라보는 방향의 델타값을 더해가면서
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
        # 커맨드 인덱스와 dir을 비교해서. 지금 보는 방향이면
        # 해당 방향 델타로 범위검사, 벽/물 검사 후 전진여부 결정
        # 아니라면 해당 dir로 변경
        else:
            if cmd_li.index(c) == dir_li.index(board[nr][nc]):
                dr, dc = delta[dir_li.index(board[nr][nc])]
                nr, nc = nr + dr, nc + dc
                if not (0 <= nr < H and 0 <= nc < W and board[nr][nc] == '.'):
                    nr, nc = nr - dr, nc - dc
                else:
                    board[nr][nc], board[nr-dr][nc-dc] = board[nr-dr][nc-dc], board[nr][nc]
            else:
                print(board[nr][nc])
                board[nr][nc] = dir_li[cmd_li.index(c)]
                print(board[nr][nc])
        for r in range(H):
            for c in range(W):
                print(board[r][c], end='')
            print()
        print('--------------')
    # print(f"#{tc} ", end='')
    # for r in range(H):
    #     for c in range(W):
    #         print(board[r][c],end='')
    #     print()
