import sys

sys.stdin = open("input.txt", "r")


def solve():
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for _ in range(10):
        t = int(input())
        board = [list(map(int, input())) for _ in range(16)]

        # if t != 1:
        #     continue

        # 시작점 검색
        def find_start():
            for r in range(16):
                for c in range(16):
                    if board[r][c] == 2:
                        return r, c

        sr, sc = find_start()

        # dfs
        result = 0
        visited = [[0] * 16 for _ in range(16)]
        stack = [(sr, sc)]
        while stack:
            tr, tc = stack.pop()
            if board[tr][tc] == 3:
                result = 1
                break
            if visited[tr][tc]:
                continue
            visited[tr][tc] = 1
            for dr, dc in delta:
                nr, nc = tr + dr, tc + dc
                if 0 <= nr < 16 and 0 <= nc < 16 and board[nr][nc] != 1:
                    stack.append((nr, nc))
        print(f"#{t} {result}")


if __name__ == "__main__":
    solve()

"""
#1 1
#2 1
#3 1
#4 0
#5 1
#6 1
#7 0
#8 1
#9 1
#10 1
"""
