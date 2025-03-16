# 호석이는 잘 생각이 없는듯하다..
# 계산 할때마다 각 자리수 index를 카운팅하는 배열 선언
# 배열 안에 0이 없을 때까지..


def cnt_num(n):
    while True:
        num_count[n % 10] += 1
        if n // 10 == 0:
            break
        n //= 10


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    i = 1
    num_count = [0] * 10
    while True:
        cnt_num(i * n)
        if 0 not in num_count:
            break
        i += 1

    print(f"#{tc} {i*n}")
