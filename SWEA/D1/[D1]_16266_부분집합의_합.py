A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    count = 0
    for i in range(1 << 12):
        total = 0
        sub_count = 0
        for j in range(12):
            if i & (1 << j):
                total += A[j]
                sub_count += 1
        if total == K and sub_count == N:
            count += 1

    print(f'#{tc} {count}')
