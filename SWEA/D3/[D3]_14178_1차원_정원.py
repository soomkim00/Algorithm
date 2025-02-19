#  water == 한 번에 물을 줄 수 있는 최대 범위
#  // 로 최대한 많은 범위에 물을 주고
#  % 로 남은 칸 확인 후 남았으면 한번 더!

T = int(input())

for tc in range(1, T + 1):
    N, D = map(int, input().split())
    water = 1 + 2 * D
    result = 0
    result += N // water
    if N % water:
        result += 1

    print(f"#{tc} {result}")
