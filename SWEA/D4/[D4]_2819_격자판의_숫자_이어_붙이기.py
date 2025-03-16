# 중복이 가능한 dfs..
# 숫자가 커지긴 한데, 격자판 사이즈가 4x4라서 할만함
# 결과값의 중복을 제거한 후 총 개수를 반환해야 하므로 결과를 set()에 저장

def dfs(r, c, depth, num):
    if depth == 7:
        result.add(num)
        return
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, depth + 1, num * 10 + board[nr][nc])


T = int(input())

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    for r in range(4):
        for c in range(4):
            dfs(r, c, 1, board[r][c])

    print(f"#{tc} {len(result)}")
