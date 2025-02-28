T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    print(f"#{t} ")
