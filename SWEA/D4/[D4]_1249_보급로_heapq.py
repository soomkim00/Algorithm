import sys

sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop


# 다ijk스트라 - heapq를 사용한
# 시작 (0,0) 도착(N-1, N-1)
# 비용 == 칸의 숫자값

def dijk():
    pq = [(0, 0, 0)]  # cost, r, c
    dists = [[float('inf')] * N for _ in range(N)]  # 최단거리 저장 리스트
    dists[0][0] = 0  # 시작점 거리 0

    while pq:
        now_dist, now_r, now_c = heappop(pq)

        # now 칸 더 작은 거리 있는지 체크
        if dists[now_r][now_c] < now_dist:
            continue

        # 인접 칸 접근
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_r, next_c = now_r + dr, now_c + dc
            # 범위 체크
            if 0 <= next_r < N and 0 <= next_c < N:
                # next 칸 누적 거리 계산 : now 칸까지 누적 거리 + next칸 비용(board)
                new_dist = now_dist + board[next_r][next_c]

                # next 칸 더 작은 거리 있는지 체크
                if dists[next_r][next_c] <= new_dist:
                    continue

                # 도착 칸이면 종료
                if next_r == N-1 and next_c == N-1:
                    return new_dist

                # dists 갱신, pq에 추가
                dists[next_r][next_c] = new_dist
                heappush(pq, (new_dist, next_r, next_c))

    return dists[N - 1][N - 1]  # 도착지점 거리 정보 return


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        board = [list(map(int, input())) for _ in range(N)]
        result = dijk()
        print(f"#{tc} {result}")

"""
#1 2
#2 2
#3 8
#4 57
#5 151
#6 257
#7 18
#8 160
#9 414
#10 395
"""