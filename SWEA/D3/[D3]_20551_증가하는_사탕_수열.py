#  가장 적게 먹고 만들 수 있는 순증가 = (c-2, c-1, c)
#  c가 2보다 작거나 b가 1보다 작으면 불가능
#  각 a, b를 c-2, c-1보다 큰 만큼 먹어서 그 총합을 return

def nyam(a, b, c):
    if c <= 2 or b <= 1:
        return -1
    cnt = 0
    if b > c - 1:
        cnt += b - (c - 1)
    if a > c - 2:
        cnt += a - (c - 2)

    return cnt


T = int(input())

for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    result = nyam(A, B, C)

    print(f"#{tc} {result}")
