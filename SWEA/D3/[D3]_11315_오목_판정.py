# 각 칸에 대해서 그 칸이 돌이 있으면
# 가로/세로/대각선/역대각선으로 검사할 수 있는가?
# 1 해당 방향 하나 전이 범위 밖이거나
# 2 '.' 이면 검사하겠다.
# 가로/세로의 경우 오목 범위까지 뻗을수 있는지 검사 후 검사
# 대각선/역대각선의 경우 해당 검사 안에서 처리
# 각 방향별 검사 후 결과 return


def check_board():
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'o':
                if (c - 1 >= 0 and board[r][c - 1] == '.' and c + 4 < N) or c == 0:
                    if check_hor(r, c):  # 가로 체크
                        return 1
                if (r - 1 >= 0 and board[r - 1][c] == '.' and r + 4 < N) or r == 0:
                    if check_ver(r, c):  # 세로 체크
                        return 1
                if (r - 1 >= 0 and c - 1 >= 0 and board[r - 1][
                    c - 1] == '.' and r + 4 < N and c + 4 < N) or r == 0 or c == 0:
                    if check_cross(r, c):  # 대각선 체크
                        return 1
                if (r - 1 >= 0 and c + 1 < N and board[r - 1][
                    c + 1] == '.' and r + 4 < N and c - 4 < N) or r == 0 or c == N - 1:
                    if check_cross2(r, c):  # 역대각선 체크
                        return 1


def check_hor(r, c):
    for d in range(1, 5):
        if board[r][c + d] == '.':
            return 0
    else:
        return 1


def check_ver(r, c):
    for d in range(1, 5):
        if board[r + d][c] == '.':
            return 0
    else:
        return 1


def check_cross(r, c):
    if r + 4 >= N or c + 4 >= N:
        return 0
    for d in range(1, 5):
        if board[r+d][c+d] == '.':
            return 0
    else:
        return 1


def check_cross2(r, c):
    if r + 4 >= N or c - 4 < 0:
        return 0
    for d in range(1, 5):
        if board[r + d][c - d] == '.':
            return 0
    else:
        return 1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    if check_board():
        print(f"#{tc} YES")
    else:
        print(f'#{tc} NO')
