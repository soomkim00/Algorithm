import sys

sys.stdin = open('input.txt', 'r')

# 가장자리 제외 코어 위치 저장
# 재귀호출 -> 각 코어에서 델타방향 뻗는경우 + 안 뻗는 경우
# 탐색 종료 후 연결 코어 개수 비교 및 길이 합 갱신

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))


def solve():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        board = [list(map(int, input().split())) for _ in range(N)]

        # if t != 1:
        #     continue

        cores = []
        for r in range(1, N - 1):
            for c in range(1, N - 1):
                if board[r][c]:
                    cores.append((r, c))

        result = float('inf')
        max_connect = 0

        def recur(idx, length, visited, connect):
            nonlocal result, max_connect

            if idx == len(cores):
                if connect > max_connect or (connect == max_connect and result > length):
                    max_connect = connect
                    result = length
                return

            recur(idx + 1, length, visited, connect)

            tr, tc = cores[idx]

            for dr, dc in delta:
                nr, nc = tr + dr, tc + dc
                path = []

                while 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] == 1 or (nr, nc) in visited:
                        break
                    else:
                        path.append((nr, nc))
                    nr += dr
                    nc += dc

                if not (0 <= nr < N and 0 <= nc < N):
                    for p in path:
                        visited.add(p)

                    recur(idx + 1, length + len(path), visited, connect + 1)

                    for p in path:
                        visited.remove(p)

        recur(0, 0, set(), 0)

        print(f"#{t} {result}")


if __name__ == '__main__':
    solve()

"""
3
7
0 0 1 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
1 1 0 1 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0
9
0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0
0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0 1
11
0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1
0 0 0 1 0 0 0 0 1 0 0
0 1 0 1 1 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
"""

"""
#1 12
#2 10
#3 24
"""
