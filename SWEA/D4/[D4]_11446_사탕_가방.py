import sys

sys.stdin = open("input.txt", "r")


def make_bag(li: list):
    global cnt
    if sum(li) < M:
        return

    if sum(li) == M:
        cnt += 1
        return

    left_li, right_li = [], []

    for num in li:
        left_li.append(num // 2)
        right_li.append(num - num // 2)

    make_bag(left_li)
    make_bag(right_li)


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        arr = list(map(int, input().split()))
        cnt = 0
        make_bag(arr)

        print(f"#{tc} {cnt}")
