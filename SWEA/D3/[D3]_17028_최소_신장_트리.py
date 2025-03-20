import sys

sys.stdin = open("input.txt", "r")

# heapq를 이용하면 heapq에서 꺼내는 순간 최소 거리임을 확정
# 즉, 방문처리만 확인하면 된다..!


import heapq


def prim(start_node):
    pq = [(0, start_node)]
    MST = [0] * (V + 1)  # 방문처리 (==visited)
    min_weight = 0

    while pq:
        # weight 최소 노드 pop
        now_w, now_n = heapq.heappop(pq)

        # 방문 체크
        if MST[now_n]:
            continue

        # 방문 처리
        MST[now_n] = 1
        # 누적합 추가
        min_weight += now_w

        # 연결 된 다음 칸들을 불러옴
        for next_w, next_n in graph[now_n]:
            # 다음 칸 방문 체크
            if MST[next_n]:
                continue

            # 힙큐에 다음 칸 집어넣기
            heapq.heappush(pq, (next_w, next_n))

    # 최종 누적합 반환
    return min_weight


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        V, E = map(int, input().split())
        graph = [[] for _ in range(V + 1)]

        # 인접 리스트[시작정점] = (가중치, 도착정점)
        for _ in range(E):
            n1, n2, w = map(int, input().split())
            graph[n1].append((w, n2))
            graph[n2].append((w, n1))

        result = prim(1)

        print(f"#{tc} {result}")
