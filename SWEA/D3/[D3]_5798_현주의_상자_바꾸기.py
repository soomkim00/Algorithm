T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    box = [0] * N
    for i in range(1, Q + 1):
        l, r = map(int, input().split())
        for x in range(l - 1, r):
            box[x] = i
    print(f"#{tc}", *box)
