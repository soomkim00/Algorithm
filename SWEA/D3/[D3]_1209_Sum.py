# import sys

# sys.stdin = open("sum_input.txt", "r", encoding="utf-8")
SIZE = 100

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(SIZE)]
    sum_list = []

    # 대각선합 역대각선합
    temp_x1 = temp_x2 = 0

    # n을 증가시키면서
    for n in range(SIZE):
        # 가로합 세로합
        temp_h = temp_v = 0

        # 행 고정, 열 증가 / 가로 합
        for j in range(SIZE):
            temp_h += arr[n][j]
        sum_list.append(temp_h)

        # 열 고정, 행 증가 / 세로 합
        for i in range(SIZE):
            temp_v += arr[i][n]
        sum_list.append(temp_v)

        # 대각선합, 역대각선합 누적
        temp_x1 += arr[n][n]
        temp_x2 += arr[n][SIZE - n - 1]

    # 반복 후 대각선/역대각선합 추가
    sum_list.append(temp_x1)
    sum_list.append(temp_x2)

    # 합계 중 가장 큰 값 출력
    print(f"#{tc} {max(sum_list)}")
