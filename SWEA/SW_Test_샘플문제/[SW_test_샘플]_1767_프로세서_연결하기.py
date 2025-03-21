import sys

sys.stdin = open("input.txt", "r")

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        board = [list(map(int, input().split())) for _ in range(N)]

        print(f"#{tc} ")
