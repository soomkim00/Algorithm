def cal_val(counts, N, M):
    for count in counts:
        if count > N // 2:
            return -1

    sum_a = sum_b = sum_c = 0
    result = []
    for i in range(2, M):
        for j in range(i + 1, M + 1):
            sum_a = sum(counts[0:i])
            sum_b = sum(counts[i:j])
            sum_c = sum(counts[j : M + 1])
            for s in [sum_a, sum_b, sum_c]:
                if s > N // 2 or s == 0:
                    break
            else:
                min_sum = min(sum_a, sum_b, sum_c)
                max_sum = max(sum_a, sum_b, sum_c)
                gap = max_sum - min_sum
                result.append(gap)
    if result == []:
        return -1
    else:
        return min(result)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))
    counts = [0] * (max(carrots) + 1)

    for carrot in carrots:
        counts[carrot] += 1

    result = cal_val(counts, N, max(carrots) + 1)

    print(f"#{tc} {result}")
