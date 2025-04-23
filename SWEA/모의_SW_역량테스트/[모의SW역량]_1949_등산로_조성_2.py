import sys

sys.stdin = open("input.txt", "r")

def main():
    T = int(input())

    # 4방향 이동(상, 하, 좌, 우)
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    for tc in range(1, T+1):
        N, K = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(N)]

        # 최고봉 높이와 위치 찾기
        max_h = max(max(row) for row in grid)
        peaks = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == max_h]

        visited = [[False]*N for _ in range(N)]
        answer = 0

        def dfs(x, y, length, cut_used):
            nonlocal answer
            # 경로 최대 길이 갱신
            if length > answer:
                answer = length

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    # 내려갈 수 있는 경우
                    if grid[nx][ny] < grid[x][y]:
                        visited[nx][ny] = True
                        dfs(nx, ny, length+1, cut_used)
                        visited[nx][ny] = False
                    # 깎아서 내려갈 수 있는 경우
                    elif not cut_used and grid[nx][ny] - K < grid[x][y]:
                        original_height = grid[nx][ny]
                        grid[nx][ny] = grid[x][y] - 1
                        visited[nx][ny] = True

                        dfs(nx, ny, length+1, True)

                        # 복원
                        grid[nx][ny] = original_height
                        visited[nx][ny] = False

        # 각 최고봉에서 DFS 시작
        for sx, sy in peaks:
            visited[sx][sy] = True
            dfs(sx, sy, 1, False)
            visited[sx][sy] = False

        print(f"#{tc} {answer}")

if __name__ == "__main__":
    main()

"""
#1 6
#2 3
#3 7
#4 4
#5 2
#6 12
#7 6
#8 7
#9 10
#10 19
"""