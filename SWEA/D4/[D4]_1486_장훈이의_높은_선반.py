import sys

sys.stdin = open("input.txt", "r")

# 비트연산으로 부분집합을 구하는데
# 들어간다 나올때마다 탑 높이 합(temp)를 구하고
# 합이 B를 넘어갔는지 체크해서 넘어갔으면 종료

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    min_gap = float('inf')
    # 비트연산으로 부분집합 j 번째 사람을 쓸것인가?
    for i in range(1 << N):
        temp = 0
        for j in range(N):
            # 엄밀히 말하면 오른쪽에서 j번째 사람을 고르는것이지만
            # 모든 부분집합을 구할 것이라서 순서는 상관 x
            if i & (1 << j):
                temp += H[j]
            # 탑 높이가 선반을 넘었는가? -> 최소 차이 갱신
            if temp >= B:
                min_gap = min(min_gap, temp - B)
                break
        temp = 0

    print(f"#{tc} {min_gap}")

"""
#1 1
#2 4
#3 27
#4 11
#5 42
#6 32
#7 2
#8 3
#9 25
#10 0
"""