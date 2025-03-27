import sys
from collections import deque

input = sys.stdin.readline


def solve():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        important = list(map(int, input().split()))
        imp_sorted = sorted(important,reverse=True)
        arr = deque()
        for i in range(N):
            arr.append((i, important[i]))
        cnt = 0
        while arr:
            temp = arr.popleft()
            if temp[1] == imp_sorted[cnt]:
                if temp[0] == M:
                    print(cnt + 1)
                    break
                cnt += 1
            else:
                arr.append(temp)


if __name__ == "__main__":
    solve()
