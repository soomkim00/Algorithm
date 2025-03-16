import sys

sys.stdin = open("input.txt", "r")


def dfs(r, c, cnt, d_idx, visited):
    global max_len
    if d_idx == 2 and cnt * 2 < max_len:
        return

    # 종료조건 방향 다 바뀌고 도착
    if (r, c) == start and d_idx == 3:
        max_len = max(max_len, cnt)
        return

    for d in (d_idx, d_idx + 1):
        if d > 3:
            return

        nr, nc = r + delta[d][0], c + delta[d][1]
        if 0 <= nr < N and 0 <= nc < N and not visited[cafe[nr][nc]]:
            visited[cafe[nr][nc]] = 1
            dfs(nr, nc, cnt + 1, d, visited)
            visited[cafe[nr][nc]] = 0


if __name__ == "__main__":
    T = int(input())
    delta = ((1, 1), (1, -1), (-1, -1), (-1, 1))  # 대각선 방향 델타 (사각형이 만들어지는 순서로)

    for t in range(1, T + 1):
        N = int(input())
        cafe = [list(map(int, input().split())) for _ in range(N)]
        max_len = -1
        # 각 지점에서 길이를 구해서
        for r in range(N - 2):
            for c in range(N - 1):
                start = (r, c)
                dfs(r, c, 0, 0, [0] * 101)

        print(f"#{t} {max_len}")
