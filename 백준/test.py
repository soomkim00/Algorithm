import sys
from collections import deque

input = sys.stdin.readline


def solve():
    N = int(input())
    stairs = [0] + list(int(input()) for _ in range(N))
    q = deque()
    q.append((0, 0, 0))  # 현재 칸, 연속된 1 개수, 총점
    memo = dict()

    while q:
        now, cnt, score = q.popleft()

        # 도착점 넘어갔는지, 연속된 세번인지
        if now > N or (cnt >= 2 and now > 2):
            continue

        temp = score + stairs[now]

        if now in memo and temp <= memo[now]:
            continue

        score = temp
        memo[now] = score

        # 전진
        q.append((now + 1, cnt + 1, score))  # 1칸 전진
        q.append((now + 2, 0, score))

    print(memo)
    print(memo[N])


if __name__ == "__main__":
    solve()
