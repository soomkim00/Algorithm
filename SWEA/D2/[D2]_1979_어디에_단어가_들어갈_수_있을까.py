# 체크 조건에 따라서 가로 단어/ 세로 단어 체크 함수 따로 구현
# 체크 조건 == 시작 칸인가 or 이전 칸이 0인가
# 단어 체크 == K 칸 동안 1이고, 그 다음이 끝 or 0인가
# 단어 체크 시 K 칸 뒤가 범위를 벗어나면 단어 안됨


def check_hor(puzzle, i, j, N, K):
    if j + K > N:
        return 0

    for n in range(1, K):
        if puzzle[i][j + n] == 0:
            return 0

    if j + K == N or puzzle[i][j + K] == 0:
        return 1
    else:
        return 0


def check_ver(puzzle, i, j, N, K):
    if i + K > N:
        return 0

    for n in range(1, K):
        if puzzle[i + n][j] == 0:
            return 0

    if i + K == N or puzzle[i + K][j] == 0:
        return 1
    else:
        return 0


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1:
                if j == 0 or puzzle[i][j - 1] == 0:
                    count += check_hor(puzzle, i, j, N, K)
                if i == 0 or puzzle[i - 1][j] == 0:
                    count += check_ver(puzzle, i, j, N, K)

    print(f"#{tc} {count}")
