from collections import deque
# import sys
#
# sys.stdin = open("input.txt", "r")

T = int(input())
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상 우 하 좌
# 터널 종류 별 방향 정보 (delta의 인덱스정보)
tunnel = {1: (0, 1, 2, 3),
          2: (0, 2), 3: (1, 3),
          4: (0, 1), 5: (1, 2),
          6: (2, 3), 7: (0, 3),
          }

for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # bfs
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append((R, C))
    visited[R][C] = 1
    cnt = 1  # 하나씩 접근할때마다 count 증가, 시작점 개수 1
    while q:
        tr, tc = q.popleft()
        # 현재 위치까지의 거리가 L이면 continue (이 지점에서 더 이상 탐색 x)
        if visited[tr][tc] == L:
            continue

        # 해당 통로에서 갈 수 있는 방향으로 델타 탐색
        for d_idx in tunnel[board[tr][tc]]:
            dr, dc = delta[d_idx]
            nr, nc = tr + dr, tc + dc
            # 범위 체크, 방문했는지, 터널인지 체크
            if 0 <= nr < N and 0 <= nc < M and not(visited[nr][nc]) and board[nr][nc]:
                # 다음 터널과 지금 보는 방향이 연결되는지 판단
                for n_idx in tunnel[board[nr][nc]]:
                    # 서로 반대 방향이면 연결되있다 == (0, 2) 이거나 (1, 3)이다.
                    # 즉, 서로 같지 않고 더한 값의 2로 나눈 나머지가 0이다.
                    if d_idx != n_idx and (d_idx + n_idx) % 2 == 0:
                        q.append((nr, nc))
                        visited[nr][nc] = visited[tr][tc] + 1
                        cnt += 1

    print(f"#{t} {cnt}")
