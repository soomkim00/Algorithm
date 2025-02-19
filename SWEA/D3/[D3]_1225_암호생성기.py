#  덱에 넣고, 하나씩 dequeue 하고 처리 후 enqueue
#  % 5 계산으로 0~4 숫자를 순환하면서 생성후 +1 하여서 사이클
#  처리한 값이 0보다 작으면, 0으로 바꾸고. enqueue 후 break

from collections import deque

for _ in range(10):
    tc = int(input())
    num_q = deque(map(int, input().split()))

    i = 0
    while True:
        temp = num_q.popleft() - (i + 1)
        if temp <= 0:
            temp = 0
        num_q.append(temp)
        i = (i + 1) % 5
        if temp == 0:
            break

    print(f"#{tc}", *num_q)
