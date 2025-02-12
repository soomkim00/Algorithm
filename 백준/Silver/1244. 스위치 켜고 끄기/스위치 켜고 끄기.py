# index s 의 스위치 상태 변환 함수
def change_switch(s):
    switches[s] = (switches[s] + 1) % 2


# 남자의 경우 s 배수만큼 방문하면서 변경
def man_switch(s):
    for i in range(s - 1, n, s):
        change_switch(i)


# 여자의 경우, 자기 자신 바꾸고
# 양 옆 비교하면서 같으면 변경
def woman_switch(s):
    idx = s - 1
    change_switch(idx)
    x = 1
    while 0 <= idx - x and idx + x < n:
        if switches[idx - x] == switches[idx + x]:
            change_switch(idx - x)
            change_switch(idx + x)
        else:
            break
        x += 1


n = int(input())
switches = list(map(int, input().split()))
t = int(input())

for _ in range(t):
    i, j = map(int, input().split())
    if i == 1:
        man_switch(j)
    else:
        woman_switch(j)

count = 0
for i in range(len(switches)):
    print(switches[i], end=" ")
    if (i + 1) % 20 == 0:
        print()
