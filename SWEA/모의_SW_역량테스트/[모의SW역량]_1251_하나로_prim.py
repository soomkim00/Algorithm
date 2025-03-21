import sys

sys.stdin = open("input.txt", "r")

# 세금 * 길이^2 를 가중치로 갖는 최소신장트리?
# 각 섬(정점)에서 모든 다른 섬으로 연결될 수 있음
# 모든 간선.. 1,000 * 1,000
# 가능..한가?
# 엣지 모두 구해서 저장하고 크루스껄

import math
from heapq import heappop, heappush


# 환경 부담금 계산 함수
def cal_cost(r, c, nr, nc):
    L = math.sqrt(abs(r - nr) ** 2 + abs(c - nc) ** 2)
    return E * L ** 2


# 프리ㅣ임
def prim(start_node):
    pq = [(0, start_node)]  # 제일 정점 노드 뽑는 우선순위 큐, 시작점 가중치 0
    MST = [0] * N  # visited
    key = [float('inf')] * N  # 각 노드 별 최소 비용을 저장 (최적화)
    cnt = 0  # MST 포함 정점 개수 (최적화)
    key[start_node] = 0  # 시작 지점 최소 비용 == 0
    min_cost = 0  # 최소 총 비용

    while pq and cnt < N:  # pq가 비지 않고, 정점을 다 고를 때 까지
        now_cost, now_node = heappop(pq)

        # 정점 선택 여부 검사
        if MST[now_node]:
            continue

        # 선택 안했으면 선택하고, 최소 비용 누적하고, cnt 증가
        MST[now_node] = 1
        min_cost += now_cost
        cnt += 1

        # 인접 정점 pq 추가
        for next_cost, next_node in graph[now_node]:
            # 인접 정점 방문 여부 검사
            if MST[next_node]:
                continue

            # 기존 key 값과 비교해서 작은 경우에만
            # key 값 업데이트 후 pq에 추가
            if key[next_node] > next_cost:
                key[next_node] = next_cost
                heappush(pq, (next_cost, next_node))

    return min_cost


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        pos_r = list(map(int, input().split()))
        pos_c = list(map(int, input().split()))
        E = float(input())

        # if tc != 2:
        #     continue

        # (r, c) 순서쌍으로 묶어서 관리
        island = []
        for i in range(N):
            island.append((pos_r[i], pos_c[i]))

        # 각 섬들에 대한 정보 저장
        graph = [[] for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):  # 대각선 반만 계산
                # i번째 섬과 j번째 섬 사이 비용 계산
                cost = cal_cost(*island[i], *island[j])
                # 양방향 그래프
                graph[i].append((cost, j))
                graph[j].append((cost, i))

        result = prim(0)
        print(f"#{tc} {round(result)}")

"""#1 10000
#2 180000
#3 1125000
#4 1953913
#5 27365366
#6 337122
#7 711268755613
#8 280157
#9 521568761
#10 34
#11 375890356686
#12 68427157
#13 21404
#14 16620885
#15 4776395492
#16 54860981981
#17 24236206202
#18 132410
#19 12876964085
#20 7016649393
"""
