# 중간 값 기준 반반 접근
# 짝수, 홀수인 경우 나눠서 각각 접근

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    cards = list(input().split())
    suffled_cards = []
    if n % 2 == 0:
        for i in range(n // 2):
            suffled_cards.append(cards[i])
            suffled_cards.append(cards[n // 2 + i])
    else:
        for i in range(n // 2 + 1):
            suffled_cards.append(cards[i])
            if n // 2 + i + 1 >= n:
                break
            suffled_cards.append(cards[n // 2 + i + 1])

    print(f"#{tc}", *suffled_cards)
