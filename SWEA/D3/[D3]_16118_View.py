for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    view_count = 0  # 리버뷰 세대수

    # 양 끝 2개 빼고 건물 > 2~len(건물)-2 범위 탐색
    # 해당 건물의 원하는 층(낮아지면서 검사할거라 따로 지정)
    # 일단 양 옆에 건물이 없어야 검사 시작(while 조건)
    # 그 옆에 건물이 있는가? 둘 다 없으면 view_count 증가
    # 한 층 내려가서 또 검사
    
    for i in range(2, len(buildings) - 2):
        building = buildings[i]
        while building > buildings[i - 1] and building > buildings[i + 1]:
            if building > buildings[i - 2] and building > buildings[i + 2]:
                view_count += 1
            building -= 1

    print(f'#{tc} {view_count}')
