# 각 숫자가 1이면 임시 합계 +1
# 0을 만나면 현 임시 합계랑 최종 최대값 비교 및 최신화
# 반복을 끝낸 후 다시 한번 비교 및 최신화 (1로 끝나는 경우)

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    sequence = list(map(int, input()))

    max_seq = 0
    temp = 0
    for i in range(len(sequence)):
        if sequence[i] == 1:
            temp += 1
        else:
            if max_seq < temp:
                max_seq = temp
            temp = 0

    if max_seq < temp:
        max_seq = temp

    print(f'#{t} {max_seq}')
