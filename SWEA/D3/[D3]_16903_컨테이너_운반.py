import sys

sys.stdin = open("input.txt", "r")

# 가장 큰 트럭이 가능한 가장 큰 화물을 싣고
# 다음 큰 트럭이 가능한 가장 큰 화물을 싣고.. 반복


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    # 큰 것 부터 접근하기 위한 내림차순 정렬
    w.sort(reverse=True)
    t.sort(reverse=True)

    # j번째 큰 화물을 넣었으면, 그 다음은 j+1번째 화물부터 탐색한다(중복 탐색 방지)
    # 왜? 어짜피 제일 큰 트럭부터 보고있으니까..
    # 정렬했기 때문에 처음부터 탐색 == 큰 것부터 탐색
    total = 0
    start = 0
    for i in range(len(t)):
        for j in range(start, len(w)):
            # 트럭에 j 번째로 큰 화물이 넣어지는가?
            if t[i] >= w[j]:
                # 다음에는 j+1번째 화물부터 비교하자
                start = j + 1
                total += w[j]
                # 하나만 넣어야 하니까 break
                break

    print(f"#{tc} {total}")
