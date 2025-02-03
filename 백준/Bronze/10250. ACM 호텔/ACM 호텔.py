# W : 가로 (1~)
# H : 세로 (1~)
# YXX or YYXX
# 1. X 작은 방
# 2. Y 작은 방

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    y, x = 1, 1
    for i in range(n - 1):  # 첫 사람은 101이니까 -1
        if y == h:  # y층 다 올라가면
            x += 1  # 옆으로 한층
            y = 1  # y는 1층으로
        else:
            y += 1  # 아니면 y로 증가

    if x < 10:
        x = "0" + str(x)  # 한자리면 0x로 변환
    print(str(y) + str(x))  # str으로 붙이기
