import sys
from _collections import deque

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())

    moves = dict()
    for _ in range(N + M):
        s, e = map(int, input().split())
        moves[s] = e

    def bfs():
        q = deque()
        visited = [False] * 101
        q.append((1, 0))  # position, count
        visited[1] = True

        while q:
            pos, cnt = q.popleft()
            for step in range(1, 7):
                next = pos + step

                # 종료 확인
                if next == 100:
                    return cnt + 1

                # 범위 확인
                if next > 100:
                    continue

                # 뱀이나 사다리 확인
                if next in moves:
                    next = moves[next]

                # 다음 칸 접근
                if next < 100 and not visited[next]:
                    q.append((next, cnt + 1))
                    visited[next] = True

    print(bfs())


if __name__ == '__main__':
    solve()