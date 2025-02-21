# 시간 별 손님 수를 모은 리스트를 만들고
# 해당 리스트를 순회한다. 이 때 인덱스는 시간값
# M초마다 현재 붕어빵에 K개를 구하고
# 해당 시간 손님 수를 뺀다
# 0보다 작아지면 실패
# 끝까지 실패하지 않으면 성공

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))

    now = 0     # 현재 붕어빵 개수
    t = 0       # 시간 정보

    c_cnt = [0] * (max(customer) + 1)

    # 시간 별 손님 수를 집계
    for c in customer:
        c_cnt[c] += 1

    for t in range(0, len(c_cnt)):
        # M초마다 K개씩
        if t != 0 and t % M == 0:
            now += K
            
        # 시간에 오는 손님 수 빼기
        now -= c_cnt[t]
        
        # 음수(실패)인지 체크
        if now < 0:
            print(f'#{tc} Impossible')
            break
    else:
        print(f'#{tc} Possible')

