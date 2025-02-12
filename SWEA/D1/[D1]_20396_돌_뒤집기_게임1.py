T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    stones = list(map(int, input().split()))
    for _ in range(m):
        i, j = map(int, input().split())
        for k in range(j):
            if i - 1 + k == n:
                break
            stones[i - 1 + k] = stones[i - 1]

    print(f"#{tc}", *stones)
