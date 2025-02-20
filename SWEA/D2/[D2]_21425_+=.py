# 가장 빨리 크는 법은
# 둘 중에 큰 놈을 더하는것

T = int(input())

for tc in range(1, T + 1):
    a, b, n = map(int, input().split())
    cnt = 0
    while a <= n and b <= n:
        if a >= b:
            b += a
        else:
            a += b
        cnt += 1

    print(cnt)
