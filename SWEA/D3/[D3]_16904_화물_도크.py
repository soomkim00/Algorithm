import sys

sys.stdin = open("input.txt", "r")

# 종료 시간이 빠른 작업부터 시행 (교재에 있는 규칙)
# 겹치지 않는 작업 중 종료 시간이 가장 빠른 작업을 다음 작업으로
# 겹치지 않는다 == 앞 작업이 끝나고 나서 수행한다
# == 앞 작업의 종료 시간 <= 다음 작업의 시작 시간 (마치는 시간과 시작하는 시간은 같아도 된다.)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    work_time = [list(map(int, input().split())) for _ in range(N)]

    # 종료시간 기준 오름차순 정렬
    work_time.sort(key=lambda x: x[1])

    # 종료시간이 빠른 작업부터 시행
    # 전체 작업 개수, 현재 마지막 작업 종료 시간 초기화
    cnt = 0
    now_end = 0
    for work in work_time:
        # 작업의 시작 시간이 현재 종료 시간보다 작으면
        # 시간이 겹치는 경우이므로, 넘어간다
        if work[0] < now_end:
            continue
        # 아니라면, 해당 작업을 수행하고, 종료 시간을 갱신
        cnt += 1
        now_end = work[1]

    print(f"#{tc} {cnt}")
