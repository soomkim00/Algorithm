# 1: N  2: S
# 위: N  아래: S

import sys

sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(N)]

    # 모든 칸을 순회하면서 자성체를 발견하면 이동시킨다
    # 이동했던 칸은 다시 탐색 안하겠다 -> 방문처리
    visited = [[0] * N for _ in range(N)]
    cnt = 0  # 결과 기록
    # 이차원 탐색
    for r in range(N):
        for c in range(N):
            if mag[r][c] == 1:
                nr, nc = r, c  # nr, nc는 다음 칸 (항상 r==nr 이지만 이해를 위해 따로 사용)
                while True:
                    nc -= 1  # 한 칸 아래
                    if nc >= N:  # 아래 범위를 벗어나면
                        mag[r][c] = 0 # 밑으로 떨어짐. 자성체 없앰
                    if mag[nr][nc] == mag[r][c]:  # 같은 극 자성체 만나면

    print(f'#{t} ')
