n = int(input())
numbers = list(map(int, input().split()))
count = 0
for number in numbers:
    check = 0
    for i in range(1, number + 1):
        if number % i == 0:
            check += 1
    if check == 2:
        count += 1
print(count)

# 단순히.. 소수의 정의 사용
# 1과 본인만 나누어 떨어지는 수
# 즉 1부터 본인까지 하나씩 나눠봤을 때
# 나머지가 0인 경우가 2번만 등장하는 수
# 의 개수를 세서 반환
