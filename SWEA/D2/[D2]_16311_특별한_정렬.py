# 리스트의 인덱스가 짝수/홀수인 경우에
# 각각 최대/최소를 고르는 선택정렬
# *** 출력 10개까지만 ***


def special_sort(a, n):
    for i in range(n - 1):
        if i % 2 == 0:
            max_idx = i
            for j in range(i, n):
                if a[max_idx] < a[j]:
                    a[max_idx], a[j] = a[j], a[max_idx]
        else:
            min_idx = i
            for j in range(i, n):
                if a[min_idx] > a[j]:
                    a[min_idx], a[j] = a[j], a[min_idx]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    special_sort(numbers, N)

    print(f"#{tc}", end=" ")
    for i in range(10):
        print(numbers[i], end=" ")
    print()
