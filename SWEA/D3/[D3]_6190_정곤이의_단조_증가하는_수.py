# 정수 두개씩 곱한 후에
# 그 곱한 값을 하나씩 순환하면서 단조 증가인지 체크
# 맞다면 현재 최솟값과 비교/최신화
# 최종 최대값 출력
# 한번도 최신화 안되면 기본값 -1 출력

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_val = -1
    for i in range(N-1):
        for j in range(i+1, N):
            num = arr[i] * arr[j]
            temp = str(num)
            for k in range(len(temp) - 1):
                if int(temp[k]) > int(temp[k + 1]):
                    break
            else:
                if max_val < num:
                    max_val = num

    print(f"#{tc} {max_val}")
