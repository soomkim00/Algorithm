#  가장 마지막에 남은 피자의 번호가 중요하기 때문에
#  원형 큐에 인덱스값을 넣고
#  dequeue할 때마다 해당 인덱스의 pizza값을 확인한다.
#  0이 아니라면 다시 해당 인덱스를 enqueue
#  0이면 다음 차례 인덱스를 enqueue
#  큐에 원소가 하나만 남아있다면. 그게 맨 마지막 피자 번호

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    fire_pot = deque()

    #  큐가 가득찰 때까지 인덱스를 채움(0부터 증가)
    idx = 0
    while len(fire_pot) < N:
        fire_pot.append(idx)
        idx += 1

    #  큐에 원소가 하나 남을 때까지 반복한다.
    while len(fire_pot) > 1:
        #  큐에서 dequeue한 값을 t_idx에 저장
        #  해당 인덱스의 피자 정보를 반으로 줄임
        #  그 후 해당 인덱스 피자 정보 조건문 처리
        t_idx = fire_pot.popleft()
        pizza[t_idx] //= 2

        #  해당 인덱스 피자 값이 0이 아니라면, 다시 euqueue
        #  0이 됐다면, idx값이 범위(피자 개수)안인지 확인 후 idx 삽입
        if pizza[t_idx] != 0:
            fire_pot.append(t_idx)
        else:
            if idx < M:
                fire_pot.append(idx)
                idx += 1

    #  하나 남은 원소가 마지막 피자의 인덱스. +1 해서 피자 번호를 출력
    result = fire_pot.popleft()
    print(f"#{tc} {result + 1}")
