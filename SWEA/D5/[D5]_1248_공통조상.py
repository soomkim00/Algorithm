# 1 공통 부모 구하기
# 1-1 주어진 두 정점의 부모를 순차적으로 올라가면서 방문한 정보를 리스트에 저장
# 1-2 두 리스트를 비교하면서 가장 먼저 발견한 같은 부모가 가장 가까운 공통 부모
# 2 서브 트리 크기 구하기
# 2-1 재귀 함수를 사용해서 dfs로 count
# 2-2 정점 본인 개수 1 + 하위 자식들로 함수 재 호출
# 2-3 맨 밑 자식들부터 count 값을 return하면서 더해가서 최종 서브 트리 개수 구함


# 해당 정점의 부모 정보를 순서대로 모은 리스트 만들기 (아래에서 위로)
def make_parent_list(n, p, pl):
    if len(p[n]) == 0:
        return
    pl.append(p[n][0])
    make_parent_list(p[n][0], p, pl)


# 공통 부모 탐색
def find_same_parent(np1, np2):
    for p1 in np1:
        for p2 in np2:
            if p1 == p2:
                return p1


# 서브 트리 개수 카운트
def cal_subtree_count(g, n):
    count = 1
    for child in g[n]:
        count += cal_subtree_count(g, child)
    return count


T = int(input())

for tc in range(1, T + 1):
    v, e, n1, n2 = map(int, input().split())
    arr = list(map(int, input().split()))

    # 각 노드 번호 인덱스에 자식 정보 저장한 리스트, 부모 정보 저장한 리스트
    graph = [[] for _ in range(v + 1)]
    parent = [[] for _ in range(v + 1)]

    for i in range(0, 2 * e, 2):
        graph[arr[i]].append(arr[i + 1])
        parent[arr[i + 1]].append(arr[i])

    # 부모 정보 저장받을 리스트
    n1_parents, n2_parents = [], []
    make_parent_list(n1, parent, n1_parents)
    make_parent_list(n2, parent, n2_parents)

    # 가까운 공통 부모 정점을 찾아서, 서브트리 개수 구하기
    same_parent = find_same_parent(n1_parents, n2_parents)
    sub_count = cal_subtree_count(graph, same_parent)

    print(f"#{tc} {same_parent} {sub_count}")
