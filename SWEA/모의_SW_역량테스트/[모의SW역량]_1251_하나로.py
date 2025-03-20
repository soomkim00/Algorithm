import sys

sys.stdin = open("input.txt", "r")

# 세금 * 길이^2 를 가중치로 갖는 최소신장트리?
# 각 섬(정점)에서 모든 다른 섬으로 연결될 수 있음
# 모든 간선.. 1,000 * 1,000
# 가능..한가?
# 엣지 모두 구해서 저장하고 크루스껄

import math


# 환경 부담금 계산 함수
def cal_cost(r, c, nr, nc):
    L = math.sqrt(abs(r - nr) ** 2 + abs(c - nc) ** 2)
    return E * L ** 2


# union-set의 대표(왕) 검색
def find_king(x):
    # 내가 왕이 될 상인가?
    if parents[x] == x:
        return x

    # 경로 압축
    parents[x] = find_king(parents[x])
    return parents[x]


# 합치기
def union(x, y):
    # 두 섬의 왕 찾기
    king_x = find_king(x)
    king_y = find_king(y)

    # 왕이 같다 == 같은 집합이다
    if king_x == king_y:
        return

    if rank[king_x] > rank[king_y]:
        parents[king_y] = king_x
    else:
        parents[king_x] = king_y

        if rank[king_x] == rank[king_y]:
            rank[king_y] += 1


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

        # 각 섬들에 대해서 모든 간선의 가중치(비용)을 구해놓자
        # i->j 와 j->i의 경우 동일, 반만 계산
        edges = []
        for i in range(N):
            for j in range(i + 1, N):  # 대각선 반만 계산
                # i번째 섬과 j번째 섬 사이 비용 계산
                cost = cal_cost(*island[i], *island[j])
                # 간선 정보 저장
                # 두 섬의 번호와 두 섬 사이의 비용이 저장됨
                edges.append((i, j, cost))

        edges.sort(key=lambda x: x[2])  # 비용 기준 오름차순 정렬
        parents = [i for i in range(N)]  # make_set: N개의 정점에 대해 자신을 부모로 초기화

        cnt = 0  # 몇 개 골라는가? -> N-1개까지 고르자
        result = 0.0  # 비용의 합
        rank = [0] * N  # rank

        # edges = (시작 섬 번호, 도착 섬 번호, cost:두 섬 사이의 비용)
        for start, end, cost in edges:
            # start와 end 연결 여부 체크 -> union set
            if find_king(start) != find_king(end):
                union(start, end)
                cnt += 1
                result += cost

                if cnt == N - 1:
                    break

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