import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def solve():
    N, M, B = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    count = dict()
    for r in range(N):
        for c in range(M):
            if data[r][c] in count:
                count[data[r][c]] += 1
            else:
                count[data[r][c]] = 1

    min_height = min(count.keys())
    max_height = max(count.keys())

    min_t = float('inf')  # 최소 시간
    max_h = 0  # 높이
    for now in range(min_height, max_height + 1):
        remain = B  # 인벤토리 현황
        temp_t = 0  # 현재 누적 시간
        flag = 1

        for k in sorted(count.keys(), reverse=True):
            if now == k:
                continue

            if now > k:
                block = ((now - k) * count[k])
                if block > remain:
                    flag = 0
                    break
                temp_t += block
                remain -= block
            else:
                block = ((k - now) * count[k])
                temp_t += block * 2
                remain += block

            if temp_t > min_t:
                flag = 0
                break

        if flag:
            if min_t == temp_t:
                max_h = max(max_h, now)
            else:
                min_t = temp_t
                max_h = now

    print(min_t, max_h)



if __name__ == '__main__':
    solve()
