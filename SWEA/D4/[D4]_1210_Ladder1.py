# import sys

# sys.stdin = open("input.txt", "r", encoding="utf-8")

SIZE = 100

for tc in range(10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(SIZE)]
    i, j = 99, ladder[99].index(2)
    dir_dt = {"up": (-1, 0), "left": (0, -1), "right": (0, 1)}
    dir = "up"

    while True:
        if j - 1 >= 0 and ladder[i][j - 1] == 1:
            dir = "left"
            while j >= 0 and ladder[i][j] == 1:
                i += dir_dt[dir][0]
                j += dir_dt[dir][1]
            dir = "up"
        if j + 1 < SIZE and ladder[i][j + 1] == 1:
            dir = "right"
            while j < SIZE and ladder[i][j] == 1:
                i += dir_dt[dir][0]
                j += dir_dt[dir][1]
            dir = "up"
        i += dir_dt[dir][0]
        j += dir_dt[dir][1]
        if j == 0:
            print(f"#{tc} {i}")

    # print(f"#{tc} ")
