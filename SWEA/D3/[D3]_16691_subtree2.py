# 각 노드의 자식 노드를 저장하는 2차원 배열을 선언해 저장
#   정점의 개수 = 간선 개수 + 1 (인덱스 0부터 시작해서 + 1)
# 저장된 트리의 시작점이 주어졌을 때. 해당 정점부터 서브트리틑 탐색
# 순회도.. 해보자..!
# 셋 다 결과는 동일!


def preorder(n: int):
    global cnt
    cnt += 1
    if edges[0][n]:
        preorder(edges[0][n])
    if edges[1][n]:
        preorder(edges[1][n])


def inorder(n: int):
    global cnt
    if edges[0][n]:
        preorder(edges[0][n])
    cnt += 1
    if edges[1][n]:
        preorder(edges[1][n])


def postorder(n: int):
    global cnt
    if edges[0][n]:
        preorder(edges[0][n])
    if edges[1][n]:
        preorder(edges[1][n])
    cnt += 1


T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    edges = [[0] * (E + 2) for _ in range(2)]

    for i in range(0, 2 * E, 2):
        if edges[0][arr[i]] == 0:
            edges[0][arr[i]] = arr[i + 1]
        else:
            edges[1][arr[i]] = arr[i + 1]

    cnt = 0
    preorder(N)
    # inorder(N)
    # postorder(N)

    print(f"#{tc} {cnt}")
