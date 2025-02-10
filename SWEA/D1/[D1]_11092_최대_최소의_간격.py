# 먼저 등장, 나중 등장
# >> 최대/최솟값 비교할 때 등호'='사용 여부로 결정

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    number = list(map(int, input().split()))
    max_num = min_num = number[0]
    max_idx = min_idx = 0

    for i in range(len(number)):
        if max_num <= number[i]:
            max_num = number[i]
            max_idx = i
        if min_num > number[i]:
            min_num = number[i]
            min_idx = i

    gap = 0
    if max_idx > min_idx:
        gap = max_idx - min_idx
    else:
        gap = min_idx - max_idx
    # gap = abs(max_idx - min_idx)

    print(f'#{t} {gap}')
