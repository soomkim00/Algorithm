import sys

sys.stdin = open("input.txt", "r")

from collections import deque

# 각 위치에서 bfs로 최대 길이 구한 후
# 현재 최대 길이와 비교해서 갱신

T = int(input())

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # if t != 1:
    #     continue

    max_len = 0
    max_num_li = []
    for r in range(N):
        for c in range(N):
            if N**2 - arr[r][c] < max_len:
                continue
            temp_len = 0
            q = deque()
            visited = [[0] * N for _ in range(N)]
            q.append((r, c))
            visited[r][c] = 1
            while q:
                tr, tc = q.popleft()
                for dr, dc in delta:
                    nr, nc = tr + dr, tc + dc
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] - arr[tr][tc] == 1:
                        visited[nr][nc] = visited[tr][tc] + 1
                        q.append((nr, nc))
                        if visited[nr][nc] > temp_len:
                            temp_len = visited[nr][nc]
            if temp_len > max_len:
                max_len = temp_len
                max_num_li = [arr[r][c]]
            elif temp_len == max_len:
                max_num_li.append(arr[r][c])

    room_num = min(max_num_li)
    print(f"#{t} {room_num} {max_len}")

"""
#1 6 8
#2 3 2
#3 149 2
#4 2 45
#5 2 23
#6 1 2
#7 1 4
#8 5 17
#9 4 2
#10 1 35
#11 2 2
#12 7 2
#13 45 2
#14 113 2
#15 12 32
#16 6 9
#17 1 4
#18 36 42
#19 204 2
#20 7 14
#21 4 2
#22 8225 2200
#23 35 3
#24 2 2
#25 613 2
#26 33 2
#27 5 5
"""
