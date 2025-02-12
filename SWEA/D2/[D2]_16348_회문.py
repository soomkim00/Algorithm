T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    palindrom = ""
    for r in range(N):
        for c in range(N - M + 1):
            for dc in range(M // 2):
                if arr[r][c + dc] != arr[r][c + M - 1 - dc]:
                    break
            else:
                palindrom = "".join(arr[r][c : c + M])

    for c in range(N):
        for r in range(N - M + 1):
            for dr in range(M // 2):
                if arr[r + dr][c] != arr[r + M - 1 - dr][c]:
                    break
            else:
                temp = []
                for i in range(M):
                    temp.append(arr[r + i][c])
                palindrom = "".join(temp)

    print(f"#{tc} {palindrom}")
