# 큰 숫자부터 정렬해서
# 세 개의 숫자를 탐색하면서
# m보다 합이 작은 경우를 모아서
# 가장 큰 값 return


def make_blackjack(cards):
    cards.sort(reverse=True)
    sum_set = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if cards[i] + cards[j] + cards[k] <= m:
                    sum_set.append(cards[i] + cards[j] + cards[k])
    return max(sum_set)


n, m = map(int, input().split())
cards = list(map(int, input().split()))
print(make_blackjack(cards))

# 비트연산 부분집합 구하기 시도... 시간초과
# max_sum = 0
# for i in range(1 << n):
#     temp = 0
#     count = 0
#     for j in range(n):
#         if i & (1 << j):
#             temp += cards[j]
#             count += 1
#     if count == 3 and temp <= m and max_sum < temp:
#         max_sum = temp
# print(max_sum)
