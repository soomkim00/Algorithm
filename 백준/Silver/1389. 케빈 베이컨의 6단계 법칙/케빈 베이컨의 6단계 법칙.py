import sys
from collections import deque

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N + 1)]  # 사람 번호 1~N

    for _ in range(M):
        s, e = map(int, input().split())
        edges[s].append(e)
        edges[e].append(s)  # 양방향

    scores = [0] * (N + 1)  # 케빈 베이컨 점수 모음

    def bfs(start):
        q = deque()
        visited = [0] * (N + 1)
        q.append(start)
        while q:
            now = q.popleft()

            for next in edges[now]:
                if not visited[next]:
                    visited[next] = visited[now] + 1
                    q.append(next)

        score = 0
        for i in range(1, N + 1):
            if i == start:
                continue
            score += visited[i]
        scores[start] = score

    for i in range(1, N + 1):
        bfs(i)

    scores[0] = float('inf')
    print(scores.index(min(scores)))


if __name__ == '__main__':
    solve()
