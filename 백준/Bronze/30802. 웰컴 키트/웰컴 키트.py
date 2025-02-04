n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

t_shirts = []
pen1 = n // p
pen2 = n % p
for size in sizes:
    if size % t == 0:
        t_shirts.append(size // t)
    else:
        t_shirts.append((size // t) + 1)

print(sum(t_shirts))
print(pen1, pen2)

# t-셔츠의 경우
# 묶음단위로 안 나눠 떨어지면(size % t == 0이 아니면)
#   하나 더 주문(+1)
# 나눠 떨어지면 몫만큼 주문
# 각 사이즈별로 계산 후 sum()해서 총 주문 수 확인
# 펜의 경우
# 묶음 주문 가능한 수 = 몫
# 개별 주문 수 = 나머지
