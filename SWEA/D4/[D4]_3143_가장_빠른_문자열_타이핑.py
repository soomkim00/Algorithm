def cal_cnt(a, b):
    n, m = len(a), len(b)

    result = n
    cnt = 0
    i = 0
    while i < (n - m + 1):
        for j in range(m):
            if a[i + j] != b[j]:
                break
        else:
            cnt += 1
            i = i + m - 1
        i += 1
    return result - cnt * (m - 1)


T = int(input())

for tc in range(1, T + 1):
    a, b = list(input().split())
    cnt = cal_cnt(a, b)

    print(f"#{tc} {cnt}")
