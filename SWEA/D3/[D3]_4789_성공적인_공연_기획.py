# 문제가 말이 좀 어려운데..
# 일어서 있는 사람: standing, 고용한 사람 수: cnt
# 일단 처음부터 일어나 있는 사람으로 standin 설정(arr[0])
# arr[i] 번째 숫자가 0이면, 일어날 사람이 없으므로, 조건 확인 안하고 continue
# 그게 아니라면 지금까지 일어나 있는 사람과 i를 비교.
# - 부족하면 부족한만큼(i-standin) 고용 (cnt +=)
# - 고용한 만큼 standing에 추가 (* cnt는 누적합이라서, i-standing을 더함!)
# 그 후 일어선 사람만큼 standing에 추가

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input()))
    standing = arr[0]
    cnt = 0

    for i in range(1, len(arr)):
        if arr[i] == 0:
            continue
        if standing < i:
            cnt += (i - standing)
            standing += (i - standing)
        standing += arr[i]
    print(f"#{tc} {cnt}")
