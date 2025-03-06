# import sys
#
# sys.stdin = open("input.txt", "r")


def shoot(sr, sc, d_idx):
    # 점수 초기화
    score = 0
    # 시작점을 기록, 왜? 시작점에 도착하면 종료해야해서!
    tr, tc = sr, sc
    print('sr, sc', sr, sc)
    while True:
        # 방향을 정하는 인덱스(d_idx)로 해당 방향의 델타를 가져와 다음 칸 좌표를 지정
        dr, dc = delta[d_idx]
        nr, nc = tr + dr, tc + dc


        print('nr, nc', nr, nc)
        print(d_idx)
        # 범위를 벗어나거나(벽) 네모 블럭을 만나면
        # 방향 반대로 꺾고, score 증가
        if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 5:
            score += 1
            d_idx = (d_idx + 2) % 4
            nr, nc = tr, tc
        # 세모 블록이면 score 증가하고, 방향에 맞게 꺾기
        elif 1 <= board[nr][nc] <= 4:
            score += 1
            if board[nr][nc] == 1:
                if d_idx in [0, 1]:
                    d_idx += 2
                    nr, nc = tr, tc
                elif d_idx == 2:
                    d_idx -= 1
                    tr, tc = nr, nc
                else:
                    d_idx += 1
                    tr, tc = nr, nc
            elif board[nr][nc] == 2:
                if d_idx in [1, 2]:
                    d_idx += 2
                    nr, nc = tr, tc
                elif d_idx == 0:
                    d_idx += 1
                    tr, tc = nr, nc
                else:
                    d_idx -= 1
                    tr, tc = nr, nc
            elif board[nr][nc] == 3:
                if d_idx in [2, 3]:
                    d_idx += 2
                    nr, nc = tr, tc
                elif d_idx == 1:
                    d_idx += 1
                    tr, tc = nr, nc
                else:
                    d_idx -= 1
                    tr, tc = nr, nc
            else:
                if d_idx in [0, 3]:
                    d_idx += 2
                    nr, nc = tr, tc
                elif d_idx == 2:
                    d_idx += 1
                    tr, tc = nr, nc
                else:
                    d_idx -= 1
                    tr, tc = nr, nc
            d_idx %= 4
        # 웜홀이면 짝 맞는 웜홀 지역으로 이동
        elif 6 <= board[nr][nc] <= 10:
            if hall[board[nr][nc]][0] == (nr, nc):
                nr, nc = hall[board[nr][nc]][1]
            else:
                nr, nc = hall[board[nr][nc]][0]
        # 다 아니면 그냥 한 칸 전진
        else:
            tr, tc = nr, nc

        # 블랙홀을 만나거나 시작 자리로 돌아왔는지 체크
        # 끝났으면 현재 점수를 점수리스트에 추가하고 종료
        if 0 <= nr < N and 0 <= nc < N and (board[nr][nc] == -1 or (nr == sr and nc == sc)):
            score_list.append(score)
            print('return', score)
            print(score_list)
            print('--------')
            return



delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상 우 하 좌

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 점수 저장할 리스트
    score_list = []

    # 한번 탐색하면서 땅 목록, 웜홀 목록을 저장
    # 웜홀은 번호에 맞는 좌표가 2개씩 있어서, 각 번호를 key로 갖는 딕셔너리로 선언
    land = []
    hall = {key: [] for key in range(6, 11)}
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                land.append((r, c))
            elif 6 <= board[r][c] <= 10:
                hall[board[r][c]].append((r, c))

    # 값이 0인 각 지점에서
    for r, c in land:
        # 네 방향으로 쏜다
        for d in range(4):
            shoot(r, c, d)

    print(f"#{tc} {max(score_list)}")
