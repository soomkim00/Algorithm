# 크기가 10이고 원소가 모두 0인 count_num 선언
# 이 리스트의 인덱스(0~9)에 따른 값을 각 숫자의 사용횟수로 측정
# 세 수를 곱한 값을 문자열로 치환(순차탐색을 위해)
# 문자열을 하나씩 탐색하면서
# count_num의 해당 숫자 인덱스 값 1 추가
# >> (0~9)인덱스 등장 횟수 측정
# count_num을 한줄에 하나씩 순서대로 출력


A = int(input())
B = int(input())
C = int(input())

mul = str(A * B * C)
count_num = [0] * 10


for j in range(len(mul)):
    count_num[int(mul[j])] += 1

for i in range(len(count_num)):
    print(count_num[i])
