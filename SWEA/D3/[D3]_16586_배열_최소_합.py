#  순열을 이용한 배열 합을 구하는데
#  가지치기를 이용한 호출 횟수 줄이기
#  어짜피 최소 합이니까
#  i번째 원소를 정할 때마다 i까지의 합을 구해서
#  그게 이미 최소합보다 크면 그냥 멈추자!

def f(i, n, s):
    global min_v
    if i == n:
        if min_v > s:
            min_v = s
    else:
        if s > min_v:
            return
        for j in range(i, n):
            p[i], p[j] = p[j], p[i]
            f(i + 1, n, s + arr[i][p[i]])
            p[i], p[j] = p[j], p[i]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(N)]
    min_v = 10000
    f(0, N, 0)

    print(f"#{tc} {min_v}")
