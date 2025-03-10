# 생각 나는대로
# 하나씩 pop 해서 안에 하나 더 있나?
# 없으면 남은애 지정 후 break
# 있으면 안에 있는 애도 삭제

"""
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    id_list = list(map(int, input().split()))
    remain = 0
    while id_list:
        temp = id_list.pop()
        if temp not in id_list:
            remain = temp
            break
        else:
            id_list.remove(temp)

    print(f"#{tc} {remain}")
"""

# XOR??
# 처음 ans가 0이고
# 거기에 id를 하나씩 XOR 해본다
# 특정 id가 두번 나오면 결국 원래대로 돌아오기 때문에 최종 ans에 영향을 주지 않는다
# 0 ^ k == k , 0 ^ k ^ k == 0
# 즉 마지막 남은 k 는 한번만 XOR 연산을 한 수

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    id_list = list(map(int, input().split()))
    ans = 0
    for i in id_list:
        ans = ans ^ i

    print(f"#{tc} {ans}")
