import sys

sys.stdin = open("input.txt", "r")

# 총 금액 -> 가능한가?
# 적당히 큰 금액 -> 이진탐색
# 금액이 이용권으로 딱 안떨어지는데.. 근사치 구해서 가까운 무언가..? 복잡하다
#

T = int(input())

for tc in range(1, T + 1):
    d, m, m3, y = map(int, input().split())
    cost = list(map(int, input().split()))
    print(d, m, m3, y)
    print(cost)

    print(f"#{tc} ")
