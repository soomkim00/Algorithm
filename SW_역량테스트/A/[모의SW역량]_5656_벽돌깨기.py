from collections import deque


#  dfs를 이용한 공 떨어뜨릴 위치 생성
def drop_ball(n, w, h, i):
    temp = list(map(list, bricks))
    if i == n:
        return
    for k in range(w):
        for r in range(h):
            if temp[r][k] != 0:
                break
        else:
            continue
        break_brick(k)



def break_brick(k):
    pass




T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]

    remain = []
    drop_ball(N, W, H, 0)

    print(f'#{tc} ')
