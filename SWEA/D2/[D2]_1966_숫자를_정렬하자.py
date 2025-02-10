T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    # 1. 버블정렬
    # for i in range(len(numbers)):
    #     for j in range(len(numbers) - i - 1):
    #         if numbers[j] > numbers[j + 1]:
    #             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # 2. 카운팅정렬
    count = [0] * (max(numbers) + 1)
    sorted_num = [0] * len(numbers)

    for i in range(n):
        count[numbers[i]] += 1

    for i in range(len(count) - 1):
        count[i + 1] += count[i]

    for i in range(len(numbers) - 1, -1, -1):
        count[numbers[i]] -= 1
        sorted_num[count[numbers[i]]] = numbers[i]

    print(f'#{tc}', *sorted_num)
