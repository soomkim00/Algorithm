# 열 방향, 행 방향 탐색하면서
# 1 등장하면 누적합 + 1
# 0 등장 혹은 끝나면 현재 누적합과 최대값 비교/최신화 후
# 누적합 0으로 최신화

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    structure = [list(map(int, input().split())) for _ in range(N)]

    max_len = 2
    temp = 0
    for r in range(N):
        for c in range(M):
            if structure[r][c] == 1:
                temp += 1
            if c == M - 1 or structure[r][c] == 0:
                if max_len < temp:
                    max_len = temp
                temp = 0
    for c in range(M):
        for r in range(N):
            if structure[r][c] == 1:
                temp += 1
            if r == N - 1 or structure[r][c] == 0:
                if max_len < temp:
                    max_len = temp
                temp = 0

    print(f"#{tc} {max_len}")
