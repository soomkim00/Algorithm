import sys

sys.stdin = open("input.txt", "r")

import heapq


def dijk(start_node):
    # 현재 계산된 노드까지의 누적 거리들을 저장할 우선순위 큐
    # 시작정점을 넣어놓고 시작. 시작 정점까지의 누적거리는 0
    pq = [(0, start_node)]
    dists = [float('inf')] * (N + 1)  # 각 정점까지의 최소거리를 저장할 리스트
    dists[start_node] = 0  # 시작 정점까지의 최소거리는 0

    while pq:
        now_dist, now_node = heapq.heappop(pq)  # 한 지점을 고른다

        # 이미 구한 현 지점의 최소거리가 지금의 거리보다 작거나 같으면, 넘어간다
        # 왜?? 현재 정점이 pq 안에 있을 때 최소 거리가 갱신될 수 있음..!
        if dists[now_node] < now_dist:
            continue

        # 현재 정점의 연결된 정점들의 정보를 가져와서 비교
        for next_info in graph[now_node]:
            # 다음 정점 정보 저장
            # next_dist == 현재
            next_dist = next_info[0]
            next_node = next_info[1]

            # 다음 정점까지의 거리 = 현재 정점까지의 거리 + 현재에서 다음 정점까지의 거리
            new_dist = now_dist + next_dist

            # 이미 구해진 다음 정점까지의 최소거리와 비교
            # 이미 구해진게 더 짧으면, 갱신 안하고 넘어간다.
            if dists[next_node] <= new_dist:
                continue

            # 아니라면, 다음 정점의 최소 거리(dists) 갱신 후 pq에 추가
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists[N]


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N, E = map(int, input().split())

        # 정보들을 인접리스트로 저장
        # 시작 정점 번호 열에 (거리, 도착 정점) 형태로 저장
        graph = [[] for _ in range(N + 1)]
        for _ in range(E):
            # 시작, 도착, 거리
            s, e, w = map(int, input().split())
            graph[s].append((w, e))

        min_dist = dijk(0)

        print(f"#{tc} {min_dist}")
