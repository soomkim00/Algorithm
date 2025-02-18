#  반 나눠서 승자 찾고
#  나머지 승자 찾고
#  하나 남을때까지 재귀
#  하나 남으면 return


def find_winner(s, e):
    if s == e:
        return s
    m = (s + e) // 2
    lw = find_winner(s, m)
    rw = find_winner(m + 1, e)

    return battle(lw, rw)


def battle(p1, p2):
    c1, c2 = card[p1], card[p2]
    if c1 == c2:
        return p1
    elif c1 - c2 == -2 or c1 - c2 == 1:
        return p1
    else:
        return p2


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    card = list(map(int, input().split()))
    winner = find_winner(0, N - 1)
    print(f"#{tc} {winner + 1}")
