# 힙에 하나씩 삽입해서 최종 힙을 만들고
# 루트 노드에 도착할때까지 하나씩 부모로 올라가면서 result에 더한다.


def enque(n):
    global idx
    idx += 1
    heap[idx] = n
    c = idx
    p = c // 2

    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    heap = [0] * (N + 1)
    idx = 0

    for n in num:
        enque(n)

    result = 0
    p = idx // 2
    while p:
        result += heap[p]
        p //= 2

    print(f"#{tc} {result}")
