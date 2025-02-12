SIZE = 8

for tc in range(1, 11):
    M = int(input())
    arr = [list(input()) for _ in range(SIZE)]
    count = 0
    for r in range(SIZE):
        for c in range(SIZE - M + 1):
            for dc in range(M // 2):
                if arr[r][c + dc] != arr[r][c + M - 1 - dc]:
                    break
            else:
                count += 1

    for c in range(SIZE):
        for r in range(SIZE - M + 1):
            for dr in range(M // 2):
                if arr[r + dr][c] != arr[r + M - 1 - dr][c]:
                    break
            else:
                count += 1

    print(f"#{tc} {count}")
