import sys

sys.stdin = open("input.txt", "r")

# 어짜피 한 칸에서 갈 수 있는 칸은 그 다음 칸..!


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # if tc != 1:
    #     continue

    # 0~n^2 까지 숫자가 옆 칸으로 갈 수 있는가?를 기록하는 배열
    visited = [0] * (N ** 2 + 1)

    # arr 각 칸에 상하좌우중 이동 가능한 칸이 있는가?를 체크해서 visited 최신화
    for r in range(N):
        for c in range(N):
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == arr[r][c] + 1:
                    visited[arr[r][c]] = 1
                    break

    # visited중 이어진 최대 길이와, 시작점을 저장
    start = 0
    max_len = 0
    temp = 0
    for i in range(len(visited)):
        if visited[i]:
            temp += 1
        else:
            temp += 1
            if temp > max_len:
                max_len = temp
                start = i - temp + 1
            temp = 0

    print(f"#{tc} {start} {max_len}")

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
