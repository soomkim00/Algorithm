# 원재야 친하게 지내자
# 살까? 말까 -> 뒤에 이거보다 비싼 가격이 있는가?
# 얼마나 이익인가? -> 이후 나오는 가장 비싼 가격 - 현재 구매가
# 뒤에서부터 최대값을 갱신하면서 탐색. 현재 최대값보다 작은 경우 차액만큼 이익

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    # 테스트케이스 하나만 테스트하는 코드
    # 입력 받은 후에 실행해야 정상적으로 작동함
    # if tc != 1:
    #     continue

    profit = 0  # 총 이익

    temp_max = price[-1]  # 매매가 (뒤에서부터 탐색할거라서 맨 뒤 값으로 초기화)
    for i in range(N - 2, -1, -1):
        if temp_max > price[i]:  # 이익 발생
            profit += temp_max - price[i]  # 최대값 - 현재 금액만큼 이익 발생
        else:  # 아니면
            temp_max = price[i]  # 최대값 갱신

    print(f"#{tc} {profit}")
