import sys

sys.stdin = open("input.txt", "r")


def solve():
    T = int(input())

    for tc in range(1, T + 1):
        data, change = map(int, input().split())
        data = list(str(data))

        max_v = 0  # 최대값
        memo = set()  #

        def recur(cnt, temp: list):
            nonlocal max_v
            # 종료조건
            if cnt == change:
                max_v = max(max_v, int(''.join(temp)))
                return

            # 메모이제이션
            if (cnt, tuple(temp)) in memo:
                return
            memo.add((cnt, tuple(temp)))



if __name__ == "__main__":
    solve()
