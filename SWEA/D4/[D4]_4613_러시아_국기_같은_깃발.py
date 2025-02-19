T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flags = [list(input()) for _ in range(N)]
    print(flags)

    print(f"#{tc} ")
