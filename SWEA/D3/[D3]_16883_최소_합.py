import sys

sys.stdin = open("input.txt", "r")

T = int(input())


def recur(r, c, temp):
    global min_sum
    # 기저조건: 도착했는가?
    if r == N - 1 and c == N - 1:
        # 최소값 갱신
        if min_sum > temp:
            min_sum = temp

    for dr, dc in [(1, 0), (0, 1)]:  # 아래, 오른쪽
        nr, nc = r + dr, c + dc
        # 범위 안에 들어오고, 현재 값 + 다음 칸의 값이 최소값보다 작을 경우에만 호출
        # 즉, 현재 값 + 다음 칸의 값이 최소값보다 커지면 굳이 탐색할 필요가 없다
        if 0 <= nr < N and 0 <= nc < N and temp + arr[nr][nc] < min_sum:
            recur(nr, nc, temp + arr[nr][nc])


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = float('inf')  # 파이썬 내장 최대값(무한대)
    recur(0, 0, arr[0][0])  # 시작지점 값을 초기값으로 주면서 호출

    print(f"#{tc} {min_sum}")
