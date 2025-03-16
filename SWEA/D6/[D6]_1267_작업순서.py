from collections import deque

for tc in range(1, 11):
    # 입력
    v, e = map(int, input().split())
    edges = list(map(int, input().split()))

    # 각 정점의 자식 정점 정보를 저장할 리스트
    # 부모 정점 개수를 count할 리스트
    graph = [[] for _ in range(v + 1)]
    parent_cnt = [0] * (v + 1)

    # 인접 리스트 생성
    # 추가되는 자녀 정점으로 count 리스트 갱신
    for i in range(0, 2 * e, 2):
        graph[edges[i]].append(edges[i + 1])
        parent_cnt[edges[i + 1]] += 1

    dq = deque()
    # count가 0 == 부모 정점이 없는 == 최상위 정점
    # 최상위 정점들을 큐에 추가
    for i in range(1, v + 1):
        if parent_cnt[i] == 0:
            dq.append(i)

    visit = []
    # 큐에서 정점을 하나씩 꺼내면서
    # 해당 정점 자녀 정점들의 count를 하나씩 감소
    # 즉, 해당 정점의 부모중 하나를 방문했다
    # count가 0인 정점 == 부모 정점을 모두 방문한 정점만 큐에 추가
    # 꺼낸 정점을 리스트에 추가해서 방문경로 생성!
    while dq:
        next = dq.popleft()
        for child in graph[next]:
            parent_cnt[child] -= 1
            if parent_cnt[child] == 0 and child not in dq:
                dq.append(child)
        visit.append(next)

    print(f"#{tc}", *visit)
