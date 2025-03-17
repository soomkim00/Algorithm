import sys

sys.stdin = open("input.txt", "r")

from collections import deque

# 0 하나를 누르면 이어진 0들과 8방향 인접한 빈칸까지 한번에 눌러짐
# 지뢰 없는 칸들을 숫자 칸으로 바꾸고
# 각 칸을 다시 순회하면서 0을 누르면 bfs로 인접 칸들까지 모두 방문처리
# 방문하지 않은 지뢰가 않은 칸수만큼 더 클릭해야함

if __name__ == "__main__":
    T = int(input())
    # 8방향 델타
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for t in range(1, T + 1):
        N = int(input())
        board = [list(input()) for _ in range(N)]

        # 지뢰 없는 모든 칸 숫자로 바꾸기
        for r in range(N):
            for c in range(N):
                if board[r][c] == '.':  # 지뢰 없는 칸이면
                    cnt = 0  # 인접 칸 지뢰 개수
                    for dr, dc in delta:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            if board[nr][nc] == '*':
                                cnt += 1
                    board[r][c] = cnt

        # 총 클릭횟수
        total = 0

        # 0인 칸과, 0인 칸에 상하좌우 칸을 방문처리
        visited = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if board[r][c] == 0 and not visited[r][c]:
                    total += 1
                    q = deque()
                    visited[r][c] = 1
                    q.append((r, c))
                    while q:
                        tr, tc = q.popleft()
                        if board[tr][tc] == 0:
                            for dr, dc in delta:
                                nr, nc = tr + dr, tc + dc
                                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                                    visited[nr][nc] = 1
                                    q.append((nr, nc))

        # 폭탄이 아닌 visited 하지 않은 칸들을 누르기
        for r in range(N):
            for c in range(N):
                if board[r][c] != '*' and not visited[r][c]:
                    total += 1

        print(f"#{t} {total}")

"""
#1 1990
#2 1574
#3 1252
#4 1080
#5 7645
#6 6378
#7 5073
#8 4093
#9 17111
#10 14683
#11 11693
#12 9135
#13 30616
#14 26184
#15 20124
#16 15225
#17 48378
#18 39769
#19 31522
#20 24196
"""
