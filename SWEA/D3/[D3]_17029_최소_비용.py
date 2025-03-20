import sys

sys.stdin = open("input.txt", "r")

# 다ijk스tra 활용
# 가중치(거리)를 조건에 따라 검사하면서 업데이트
# 이차원 배열에서의 적용, (가중치, r값, c값) heapq에 저장
# 시작점: (0,0,0)  |  도착점: (N-1,N-1,result)

import heapq

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 델타


def dijk(start_r=0, start_c=0):
    pq = [(0, start_r, start_c)]  # 우선순위큐
    dists = [[float('inf')] * N for _ in range(N)]  # 각 정점까지의 누적 최소 거리
    dists[start_r][start_c] = 0  # 시작점에서부터 시작점까지의 최소 거리 == 0

    # 탐색
    while pq:
        now_d, now_r, now_c = heapq.heappop(pq)  # 거리, r, c 하나 꺼내기

        # 가장 먼저 검사하는 조건: 꺼낸 now 정점에 대한 거리 now_d가 앞서 계산한 최소거리보다 작은가?
        if dists[now_r][now_c] < now_d:  # "<=" 안됨.. 왜인지는 직접 물어봐여..
            continue

        # 인접 칸들을 불러오자 어디로 이동 할 수 있는가? -> 상하좌우 -> 델타 -> 범위 검사부터!
        for dr, dc in delta:
            next_r, next_c = now_r + dr, now_c + dc  # 현재 칸 상하좌우 칸
            if 0 <= next_r < N and 0 <= next_c < N:  # 범위검사
                # 가중치 계산: 기본 1, 높이 차이만큼 추가 연료 발생
                next_d = 1
                if board[next_r][next_c] > board[now_r][now_c]:
                    next_d += board[next_r][next_c] - board[now_r][now_c]

                # 최종 가중치 == 현재(now)까지의 가중치 + 현재->다음칸 가중치
                new_d = now_d + next_d

                # 현재 계산 가중치와 이미 구한 최소값 비교
                if dists[next_r][next_c] <= new_d:
                    continue

                # 지금 구한 가중치가 더 작다면 갱신 후 인접 좌표 힙에 추가
                dists[next_r][next_c] = new_d
                heapq.heappush(pq, (new_d, next_r, next_c))

    # 탐색 끝난 후의 마지막 좌표의 거리 값 반환
    return dists[N - 1][N - 1]


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        board = [list(map(int, input().split())) for _ in range(N)]
        result = dijk()

        print(f"#{tc} {result}")
