import sys

sys.stdin = open("input.txt", "r")



def recur(cnt, score, cal):
    global masitda
    # 기저조건
    if cnt == N:
        masitda = max(masitda, score)
        return

    if cal + hambugar[cnt][1] <= L:
        recur(cnt + 1, score + hambugar[cnt][0], cal + hambugar[cnt][1])
    recur(cnt + 1, score, cal)


T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    hambugar = [list(map(int, input().split())) for _ in range(N)]
    masitda = 0

    recur(0, 0, 0)

    print(f"#{tc} {masitda}")

"""
#1 750
"""
