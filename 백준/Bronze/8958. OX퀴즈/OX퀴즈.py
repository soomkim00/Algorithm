# O가 등장하면 더하는 수를
# 등장 점수 1 + 누적 점수 로 나눠서 접근
# 등장할때마다 점수 1 증가, 쌓인 누적 점수 추가. 이후 누적 점수 1 증가

T = int(input())

for _ in range(T):
    result = input()
    temp_sum = 0
    total = 0

    for i in range(len(result)):
        if result[i] == "O":
            total += 1
            total += temp_sum
            temp_sum += 1
        else:
            temp_sum = 0
    print(total)
