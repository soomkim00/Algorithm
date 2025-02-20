# W:0 / B:1 / R:2

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flags = [list(input()) for _ in range(N)]

    c_line = []  # 각 가로줄 별 가장 많이 나온 색
    c_cnt = [[0] * N for _ in range(3)]  # 각 색이 각 가로줄마다 몇 번이 나왔는가?
    color = ['W', 'B', 'R']  # 색상을 인덱스로 쓰기 위해 리스트 선언

    for r in range(N):
        for c in range(M):
            idx = color.index(flags[r][c])  # 해당 위치 깃발 색상을 인덱스화
            c_cnt[idx][r] += 1  # 이 색상이 r번째 가로줄 등장 횟수 1 증가

        # 가로줄 한번 탐색할때마다, c_line 갱신
        # c_line : r 번째 줄에 가장 많이 등장한 색(idx)
        max_cnt = 0
        max_idx = 0
        for i in range(3):
            if max_cnt < c_cnt[i][r]:
                max_cnt = c_cnt[i][r]
                max_idx = i
        c_line.append(max_idx)

    # 각 줄에 가장 많이 등장한 색 리스트 중에 (c_line)
    # i 번째 색상이 한번도 최대로 등장하지 않았다면
    # i 번째 색상이 가장 많이 등장한 줄을 해당 색으로 칠하기로 결정
    for i in range(3):
        if i not in c_line:
            idx = c_cnt[i].index(max(c_cnt[i]))  # i 번째 색상이 가장 많이 나온 가로줄 번호
            c_line[idx] = i     # 해당 가로줄에 i번째 색을 지정하겠다

    cnt = 0
    print(c_line)
    for i in range(len(c_line)):
        cnt += (M - c_cnt[c_line[i]][i])
        print('c_cnt, c_line[i], i, cnt')
        print(c_cnt[c_line[i]][i], c_line[i], i, cnt)


    print(f"#{tc} {cnt}")
