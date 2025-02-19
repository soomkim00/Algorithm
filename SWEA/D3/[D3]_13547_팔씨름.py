#  현재 나온 o 의 개수 + 앞으로 나올 수 있는 o의 개수 >= 8 이면 가능
#  앞으로 나올 수 있는 개수: 15 - 지금까지 한 승부의 개수

T = int(input())

for tc in range(1, T + 1):
    arr = input()
    cnt = 0
    for s in arr:
        if s == 'o':
            cnt += 1

    if cnt + (15 - len(arr)) >= 8:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
