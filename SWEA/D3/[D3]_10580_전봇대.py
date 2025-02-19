# 전선이 언제 겹치는가?
# 두 전선의 양 끝의 상하 관계가 반대면
# A1 < A2 and B1 > B2 거나 그 반대의 경우에
# 전선이 서로 겹친다
# 그렇게 중복되지않게 각 전선끼리 비교를 해준 후 겹친 수 출력

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if lines[i][0] < lines[j][0] and lines[i][1] > lines[j][1]:
                cnt += 1
            elif lines[i][0] > lines[j][0] and lines[i][1] < lines[j][1]:
                cnt += 1

    print(f"#{tc} {cnt}")
