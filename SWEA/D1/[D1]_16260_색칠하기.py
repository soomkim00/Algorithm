T = int(input())
SIZE = 10

for tc in range(1, T + 1):
    arr = list([0] * SIZE for _ in range(SIZE))
    N = int(input())

    # 해당 범위에 해당 색깔의 값(1,2)만큼 더함
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[i][j] += color

    # 모든 칸을 돌면서 색의 합이 3인 부분만 count
    # 같은 색이 겹치는 경우는 없으므로
    total = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if arr[i][j] == 3:
                total += 1

    print(f'#{tc} {total}')
