N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

color1 = ['W', 'B']
color2 = ['B', 'W']

cnt = 50 * 50
for r in range(N - 7):
    for c in range(M - 7):
        cnt1 = 0
        cnt2 = 0
        for i in range(8):
            idx = i % 2
            for j in range(8):
                if board[r + i][c + j] != color1[idx]:
                    cnt1 += 1
                if board[r + i][c + j] != color2[idx]:
                    cnt2 += 1
                idx = (idx + 1) % 2
        cnt = min(cnt, min(cnt1, cnt2))


print(cnt)
