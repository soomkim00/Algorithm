T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_list = []

    for i in range(len(arr) - M + 1):
        s = 0
        for j in range(M):
            s += arr[i + j]
        sum_list.append(s)

    min_sum, max_sum = sum_list[0], sum_list[0]

    for i in range(len(sum_list)):
        if min_sum > sum_list[i]:
            min_sum = sum_list[i]
        if max_sum < sum_list[i]:
            max_sum = sum_list[i]

    print(f'#{tc + 1} {max_sum - min_sum}')
