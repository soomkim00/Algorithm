def make_parent_list(n, p, pl):
    if not p[n]:
        return
    pl.append(p[n])
    make_parent_list(p[n], p, pl)


def find_same_parent(np1, np2):
    for p1 in np1:
        for p2 in np2:
            if p1 == p2:
                return p1


def cal_subtree_count(g, n):
    count = 1
    for child in g[n]:
        count += cal_subtree_count(g, child)
    return count


T = int(input())

for tc in range(1, T + 1):
    v, e, n1, n2 = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [0 for _ in range(v + 1)]
    parent = [0 for _ in range(v + 1)]

    for i in range(0, 2 * e, 2):
        graph[arr[i]] = [i + 1])
        parent[arr[i + 1]].extend(arr[i])

    print(parent, graph)
    n1_parents, n2_parents = [], []
    # 모든 부모 정보 추가하기!
    make_parent_list(n1, parent, n1_parents)
    make_parent_list(n2, parent, n2_parents)

    print()
    same_parent = find_same_parent(n1_parents, n2_parents)
    sub_count = cal_subtree_count(graph, same_parent)

    print(f"#{tc} {sub_count}")
