import sys
from collections import deque

input = sys.stdin.readline


def solve():
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        visited = [False] * 10000

        q = deque()
        q.append((a, ""))  # (숫자 값(바뀜), 명령문)
        visited[a] = True

        while q:
            now_num, now_cmd = q.popleft()

            # 종료 조건
            if now_num == b:
                print(now_cmd)
                break

            # DSLR 탐색
            for func, cmd in ((D, 'D'), (S, 'S'), (L, 'L'), (R, 'R')):
                next_num = func(now_num)
                if not visited[next_num]:
                    visited[next_num] = True
                    q.append((next_num, now_cmd + cmd))

    return


def D(n: int):
    return 2 * n % 10000


def S(n: int):
    if n == 0:
        return 9999
    else:
        return n - 1


def L(n: int):
    left = n // 1000
    right = n % 1000
    return right * 10 + left


def R(n: int):
    left = n // 10
    right = n % 10
    return right * 1000 + left


if __name__ == "__main__":
    solve()
