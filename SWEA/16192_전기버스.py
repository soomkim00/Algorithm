T = int(input())

for t in range(T):
    k, n, m = map(int, input().split())
    station_list = list(map(int, input().split()))

    # 위치 0 ~ 정류장 위치 10 까지 0으로 된 리스트에
    # 그 중 충전기 위치를 1로 변경해서 표시
    station_pos = [0] * (n + 1)
    for i in range(len(station_list)):
        station_pos[station_list[i]] += 1

    # 버스의 위치를 표현하는 pos, 이동횟수를 표시하는 count 변수
    # 출발시에는 충전 횟수 카운팅 안하므로, 총 이동 횟수 - 1이 충전 횟수!
    pos = 0
    count = 0

    # 도착하면 종료. 일단 무한반복
    while True:
        # k 만큼 이동할 다음 위치 지정
        next_pos = pos + k

        # 만약 다음 위치가 정류장보다 크거나 같다면. 이동 횟수 증가 후 종료
        if next_pos >= n:
            count += 1
            break

        # 이동거리 안에 충전기가 있는지 검사
        # 현재위치~이동위치 탐색하며
        # station_pos를 확인해 충전기가 있으면
        # 충전기 위치를 현재 위치로
        # 여러개 발견하면 가장 멀리 있는 충전기 위치로 설정(순차방문)
        for i in range(pos, next_pos + 1):
            if station_pos[i] == 1:
                pos = i
        count += 1
        
        # 탐색 이후 현재 위치가 변하지 않았다면
        # 그 안에 충전기가 없다는 말이니까 종료
        # 충전기 없으면 출력을 0으로 해야 하니까
        # count 값을 1로 설정 (충전 횟수=이동횟수 - 1!)
        if pos == next_pos - k:
            count = 1
            break
    
    # 각 케이스 별 이동 횟수 - 1 = 충전 횟수 표시
    print(f'#{t + 1} {count - 1}')
