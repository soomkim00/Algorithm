T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    #  arr로 가득 차 있는 원형 큐 생성
    #  원형 큐에선 front가 비어있어야 하므로 맨 앞에 0 한 칸 추가
    #  가득 차 있기 때문에 rear는 마지막 idx로 지정
    cq = [0] + arr
    front = 0
    rear = N

    #  m번 동안 dequeue한 값을 enqueue
    for _ in range(M):
        #  temp에 cq에서 dequeue한 값 추가
        front = (front + 1) % len(cq)
        temp = cq[front]

        #  temp를 cq에 enqueue
        rear = (rear + 1) % len(cq)
        cq[rear] = temp

    #  작업 후 맨 앞의 있는 숫자를 dequeue로 접근해서 출력
    front = (front + 1) % len(cq)
    result = cq[front]
    print(f"#{tc} {result}")
