# 각 r 번째 줄에 접근할 c 값들을 c_list에 추가/삭제
# 처음엔 항상 중앙값(N//2), 그 후로 절반까지는 양 옆으로 1씩 벌어졌다가 줄어듦

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    value = [list(map(int, input())) for _ in range(N)]
    nc_l = N // 2 - 1
    nc_r = N // 2 + 1
    c_list = [N // 2]

    total = 0

    for r in range(N):
        for c in c_list:
            total += value[r][c]

        if r < N // 2:
            c_list.extend([nc_l, nc_r])
            nc_l -= 1
            nc_r += 1
        elif r < N - 1:
            nc_l += 1
            nc_r -= 1
            c_list.remove(nc_l)
            c_list.remove(nc_r)

    print(f"#{tc} {total}")
