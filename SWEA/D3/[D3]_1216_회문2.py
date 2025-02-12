SIZE = 100

for _ in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(SIZE)]
    result = []
    for r in range(SIZE):
        for c in range(SIZE):
            m = 2
            while c + m <= SIZE:
                for dc in range(m // 2):
                    if arr[r][c + dc] != arr[r][c + m - 1 - dc]:
                        break
                else:
                    result.append(m)
                m += 1

    for c in range(SIZE):
        for r in range(SIZE):
            m = 2
            while r + m <= SIZE:
                for dr in range(m // 2):
                    if arr[r + dr][c] != arr[r + m - 1 - dr][c]:
                        break
                else:
                    result.append(m)
                m += 1

    print(f"#{tc} {max(result)}")
