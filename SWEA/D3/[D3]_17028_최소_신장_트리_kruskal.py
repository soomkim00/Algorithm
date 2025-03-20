import sys

sys.stdin = open("input.txt", "r")


def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        V, E = map(int, input().split())

        # 시작, 끝, 가중치 간선 정보로 저장
        edges = []
        for _ in range(E):
            s, e, w = map(int, input().split())
            edges.append((s, e, w))

        edges.sort(key=lambda x: x[2])  # 가중치 정보 기준 오름차순
        parents = [i for i in range(V + 1)]  # make_set (정점 기준)

        cnt = 0  # 선택한 간선의 개수
        result = 0  # 가중치 합

        # 각 간선을 골라서
        for s, e, w in edges:
            # s와 e가 연결 되있는가? -> union set
            # 연결 안 돼 있으면 연결
            if find_set(s) != find_set(e):
                union(s, e)
                cnt += 1
                result += w

                if cnt == V:
                    break

        print(f"#{tc} {result}")
