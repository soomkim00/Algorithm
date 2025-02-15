# 666부터 검사 (그 전에는 종말의 수 안나옴)
# i를 1씩 증가시키면서 str(i) 안에 '666'이 있는지 체크
# 있으면 카운트 증가하고, 카운트가 목표 달성했는지 체크

N = int(input())

i = 666
count = 0
while True:
    if '666' in str(i):
        count += 1
    if count == N:
        print(i)
        break
    i += 1
