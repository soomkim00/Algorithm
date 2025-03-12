# 0 ~ N-1 까지 구역 (0:사무실, 1~N-1:관리구역)
# 시작 0, 끝 0이고, 그 사이에 방문할 관리구역의 순서를 중복 없이 생성 -> 순열
# 호출 전에, 현재까지의 값의 합이 구해놓은 최소값보다 커지면 호출 안함 -> 가지치기

import sys

sys.stdin = open("input.txt", "r")

T = int(input())


def recur(cnt, temp_sum):
    global min_sum

    if cnt == N - 1:  # 관리구역을 다 봤으면, 마지막 사무실까지의 비용을 추가
        temp_sum += e[path[-1]][0]
        if min_sum > temp_sum:  # 최소값 최신화
            min_sum = temp_sum

    # 1~n-1 까지의 관리구역으로 순열 생성
    for num in range(1, N):
        # 중복 체크
        if used[num]:
            continue

        used[num] = True
        path.append(num)
        # 지금까지 찾은 경로의 합이 현재 최소값보다 작을때만 호출
        # == 지금까지 찾은 경로의 합이 이미 최소값보다 크면, 더 이상 호출 필요 x
        if temp_sum + e[path[-2]][path[-1]] < min_sum:
            recur(cnt + 1, temp_sum + e[path[-2]][path[-1]])
        path.pop()
        used[num] = False


for tc in range(1, T + 1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    used = [False] * N
    min_sum = 200 * 100  # 문제 범위에서 나올 수 없는 임의의 최대값
    path = [0]  # 첫 시작은 항상
    recur(0, 0)
    print(f"#{tc} {min_sum}")
