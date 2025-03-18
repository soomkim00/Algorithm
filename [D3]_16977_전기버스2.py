import sys

sys.stdin = open("input.txt", "r")


# pos: 버스 위치, cnt: 교환 횟수
# 각 정류장에서 현재 충전지로 갈 수 있는 가장 멀리 있는 곳부터 재귀호출
# 현재 교환값이 최소값보다 크거나 같으면 종료 (가지치기)
# 버스 위치가 도착지보다 크거나 넘어가면 종료 (종료조건)
# === dp! (메모이제이션) ===
# 각 정류장까지의 최소값을 저장한 n-1 크기의 배열을 만들고
# 탐색 시 탐색하고 있는 정류장까지의 최소값과 현재 cnt를 비교해서 작을 경우만 탐색을 이어간다.
# == 현재까지의 최소값이 아니라면, 앞으로의 탐색이 의미가 없다

def go(pos, cnt):
    global min_v
    # 가지치기
    if cnt >= min_v:
        return

    # 종료조건
    if pos >= N - 1:
        min_v = min(min_v, cnt)
        return

    # 가지치기 (dp)
    if dp[pos] and dp[pos] <= cnt:
        return
    else:
        dp[pos] = cnt

    # 재귀호출
    # 현재 위치에서 갈 수 있는 정류장 중에 멀리 있는 곳부터 호출
    # 왜? 탐욕적 접근으로.. 멀리 있는 정류장 고르는게 답에 가까울 확률이 높지 않나?
    # 가장 먼 정류장 == pos + data[pos]
    for i in range(data[pos], 0, -1):
        go(pos + i, cnt + 1)


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        data = list(map(int, input().split()))
        N = data[0]
        data = data[1:]  # 정류장 번호 0 ~ N-2, N-1은 도착지라 정보 없음

        dp = [0] * N
        min_v = float('inf')  # 최소 교환 횟수
        go(0, 0)

        print(f"#{tc} {min_v - 1}")
