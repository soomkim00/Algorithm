# 각 정류장 정보를 개별 리스트로 저장 후
# 각 버스가 정류장 값 범위 안에 있는지 확인
# 포함되면 결과 1 증가

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    stops = []

    for _ in range(N):
        stop = list(map(int, input().split()))
        stops.append(stop)
    p = int(input())
    bus = []
    for _ in range(p):
        bus.append(int(input()))

    result = [0] * p

    for i in range(len(bus)):
        for stop in stops:
            if stop[0] <= bus[i] <= stop[1]:
                result[i] += 1

    print(f'#{t}', end=' ')
    for num in result:
        print(num, end=' ')
    print()
