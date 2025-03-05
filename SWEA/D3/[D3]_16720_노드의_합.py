# 두 사직 노드의 합을 부모 노드에
# 즉, L R V 순으로 방문해서 작업을 처리해야 한다.
# 후위순회!


def postorder_sum(n: int):
    # 이미 값이 있다면. 즉 계산한 값이라면 그 값 반환
    if nord[n]:
        return nord[n]

    # 범위를 넘어가면 더하지 않을거라서. 일단 0으로 초기화
    left = right = 0
    if 2 * n <= N:
        left = postorder_sum(2 * n)
    if 2 * n + 1 <= N:
        right = postorder_sum(2 * n + 1)

    # 왼쪽 자식 + 오른쪽 자식 (있다면)
    nord[n] = left + right
    return nord[n]


T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    nord = [0] * (N + 1)
    for _ in range(M):
        i, val = map(int, input().split())
        nord[i] = val

    postorder_sum(1)

    print(f"#{tc} {nord[L]}")
