T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    min_num, max_num = numbers[0], numbers[0]

    for i in range(len(numbers)):
        if min_num > numbers[i]:
            min_num = numbers[i]
        if max_num < numbers[i]:
            max_num = numbers[i]

    print(f'#{test_case} {max_num - min_num}')
