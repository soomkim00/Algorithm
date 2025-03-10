# 1: N  2: S
# 위: N  아래: S
# 일단 바닥이나 천장으로 떨어지는 애들 없애고
# 남은 애들 세로 방향으로 다른 점을 만나면 교착 상태 1개 추가
# ++ 자성체를 이동시키려다가.. 여러번 이동해야 하는 경우 처리가 어려워서. 굳이 이동 안해도 된다!

import sys

sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(N)]

    # 디버깅 코드 (테케 1만 사용)
    # if t != 1:
    #     continue

    # 없어지는 애들 없애기
    for r in range(N):
        for c in range(N):
            if mag[r][c] == 1:  # N극 자성체 -> 아래 방향 걸리는게 없으면 삭제
                for nc in range(c + 1, N):  # 한 칸 아래부터 맨 아래까지
                    if mag[r][nc]:  # [r][nc]가 0이 아니다 == 자성체다
                        break
                else:  # 자성체가 하나도 없었다 == 바닥으로 떨어진다
                    mag[r][c] = 0
            elif mag[r][c] == 2:  # S극은 반대로
                for nc in range(c):  # 0부터 c-1까지 (탐색 방향 중요x 하나도 없는지만 체크할거라서..!)
                    if mag[r][nc]:
                        break
                else:
                    mag[r][c] = 0

    # 디버깅 출력
    # for i in range(N):
    #     print(*mag[i])

    # 자성체 발견 시 아래방향 탐색하면서 다른 극을 만나면 교착 수 1 증가 후 종료
    # 위 아래로 만나야 1번의 교착이기때문에, 아래방향만 탐색하면 총 교착 수 구해짐
    # 같은 극을 만나면 교착 x 탐색 종료. 다른 극 만나면 교착+1 탐색 종료
    cnt = 0
    for r in range(N):
        for c in range(N):
            if mag[r][c] == 1:  # N극이면 아래쪽으로 탐색
                for nc in range(c+1, N):
                    if mag[r][nc] == 1:  # 같은 극을 만나면 교착 x
                        break
                    elif mag[r][nc] == 2:  # 다른 극을 만나면 교착 수 증가
                        cnt += 1
                        break
            elif mag[r][c] == 2:  # S극이면 위쪽으로 탐색
                for nc in range(c-1, -1, -1):
                    if mag[r][nc] == 2:
                        break
                    elif mag[r][nc] == 1:
                        cnt += 1
                        break

    print(f'#{t} {cnt}')

"""
#1 471
#2 446
#3 469
#4 481
#5 481
#6 501
#7 488
#8 476
#9 464
#10 490
"""
