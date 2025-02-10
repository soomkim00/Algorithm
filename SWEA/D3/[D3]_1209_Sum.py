import sys

sys.stdin = open("sum_input.txt", "r", encoding="uft-8")
SIZE = 100

for tc in range(1, 11):
    arr = [list(map(int, input().split())) for _ in range(SIZE)]

    print(f"#{tc} {data}")
