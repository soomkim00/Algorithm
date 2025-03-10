# 각 복도 번호 (room 번호 + 1) // 2
# 복도 번호에 겹치는 경로 수를 세서
# 겹치는 경로 수의 최대값 출력

# import sys
#
# sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    # 좌우 경계 확인을 위한 리스트
    boundary = []
    for i in range(N):
        i_l = (rooms[i][0] + 1) // 2
        i_r = (rooms[i][1] + 1) // 2
        if i_l > i_r:
            i_l, i_r = i_r, i_l
        boundary.append((i_l, i_r))

    # i 번 복도에 겹치는 경로의 수
    cross_cnt = [0] * 201
    for i in range(N):
        for j in range(boundary[i][0], boundary[i][1] + 1):
            cross_cnt[j] += 1
    print(f"#{tc} {max(cross_cnt)}")
