import sys
from collections import Counter
from heapq import heappush, heappop

input = sys.stdin.readline


def solve():
    T = int(input())
    for _ in range(T):
        k = int(input())
        min_hq = []
        max_hq = []
        cnt = Counter()

        for _ in range(k):
            cmd, num = input().split()

            if cmd == "I":
                heappush(min_hq, int(num))
                heappush(max_hq, -int(num))
                cnt[int(num)] += 1
            elif not cnt:
                continue
            elif num == '1':
                while True:
                    max_num = -heappop(max_hq)
                    if cnt[max_num]:
                        cnt[max_num] -= 1
                        if not cnt[max_num]:
                            del cnt[max_num]
                        break
            elif num == '-1':
                while True:
                    min_num = heappop(min_hq)
                    if cnt[min_num]:
                        cnt[min_num] -= 1
                        if not cnt[min_num]:
                            del cnt[min_num]
                        break

        if not cnt:
            print('EMPTY')
        else:
            print(max(cnt), min(cnt))


if __name__ == '__main__':
    solve()
