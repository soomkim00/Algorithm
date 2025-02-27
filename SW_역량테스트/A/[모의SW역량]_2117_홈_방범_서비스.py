T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    houses = [list(map(int, input().split())) for _ in range(N)]

    # 집 개수 구하기
    cnt_house = 0
    for r in range(N):
        for c in range(N):
            if houses[r][c] == 1:
                cnt_house += 1

    # 최대 집 개수, 범위 (범위 1일때 한 집은 무조건 가능)
    max_house = 1
    k = 1

    # 범위를 증가시키면서 탐색
    # 최대 수익(집 수 * M)이 범위 k 발생하는 cost보다 작은 동안
    while cnt_house * M >= k ** 2 + (k - 1) ** 2:
        # 범위에 해당하는 비용
        cost = k ** 2 + (k - 1) ** 2

        # 범위 1 증가
        # 시작점부터 거리가 k-1까지 bfs
        k += 1

        temp_cnt = 0
        # 집 탐색하기 -> 각 지점 별 범위 내 집 개수 구해서 temp_cnt
        pass

        # 범위 내의 집이 최대 집 개수보다 작으면 통과
        if temp_cnt < max_house:
            continue
        # 범위 내의 집에서 받을 수익이 지출보다 작으면 통과
        elif temp_cnt * M < cost:
            continue
        # 아니면 max_house 갱신
        else:
            max_house = temp_cnt

        # 만약 집 최대값이 전체 집 수와 같아지면 더 이상 비교 불필요
        if max_house == cnt_house:
            break

    print(k)
    print(f"#{tc} {max_house}")
