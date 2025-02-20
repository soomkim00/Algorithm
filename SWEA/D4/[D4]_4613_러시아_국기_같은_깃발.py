# 완전탐색 (like 당근포장)
# 위에서부터 W, B, R 이 하나 이상씩 있어야 하니까
# 행 크기 N을 1 이상의 세 조각으로 자를 두 인덱스 i,j를 생성
# 각 인덱스로 자른 줄들을 탐색하면서
# 각 줄에서 해당 색이 아닌 갯수만큼 변화할 개수
# 모든 케이스에 대해 탐색 후 최솟값 출력

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flags = [list(input()) for _ in range(N)]
    result = []

    for i in range(0, N - 2):
        for j in range(i + 1, N - 1):
            cnt = 0
            for w in range(0, i + 1):
                for x in range(M):
                    if flags[w][x] != 'W':
                        cnt += 1

            for b in range(i + 1, j + 1):
                for x in range(M):
                    if flags[b][x] != 'B':
                        cnt += 1

            for r in range(j + 1, N):
                for x in range(M):
                    if flags[r][x] != 'R':
                        cnt += 1

            result.append(cnt)

    print(f"#{tc} {min(result)}")
