# 두 개의 로봇, 두 개의 독립된 복도..
# 각 로봇의 위치와 시간 정보를 기록해서
# 각 시간에 어느 위치에 있었는지를 저장
# 1. 버튼 값에 따라서 지금 시간에 로봇이 해당 버튼까지 이동할 수 있었는지를
#   1-1 (현재 시간-로봇 이전 시간) 과 (버튼 위치 - 로봇 이전 위치)를 비교해서
#   1-2 이미 도착해있는가? 아닌가? 를 먼저 판단
# 2. 아니라면
#   

def cmd_robot(name: str, btn: int):
    global time

    if name == "B":
        n = Blue
    else:
        n = Orange

    if time - n['time'] > abs(btn - n['pos']):
        time += 1
    elif time < abs(btn - n['pos']) + 1:
        time = abs(btn - n['pos']) + 1
    else:
        time += abs(btn - n['pos']) + 1
    n['time'] = time
    n['pos'] = btn


T = int(input())

for tc in range(1, T + 1):
    arr = list(input().split())
    N = arr[0]
    command = arr[1:]
    Orange = {'pos': 1, 'time': 0}
    Blue = {'pos': 1, 'time': 0}
    time = 0

    for i in range(0, len(command), 2):
        cmd_robot(command[i], int(command[i + 1]))
        # 디버깅 출력
        print('n, btn', command[i], command[i+1])
        print('Orange', Orange)
        print('Blue', Blue)
        print('time', time)
        print('-----------')

    print(f"#{tc} {time}")