# 방문 수 늘어나는 규칙 보면
# 1 + 6 * (1부터 i까지의 합) 범위 안에 들어오면
# i + 1만큼 방문함
# 1~i의 합을 함수로 구하고
# 무한루프로 1부터 증가시켜가면서 체크


def make_sum(n):
    result = 0

    for i in range(1, n + 1):
        result += i

    return result


N = int(input())
i = 1

while True:
    if N == 1:
        print(1)
        break

    if N <= 1 + 6 * make_sum(i):
        print(i + 1)
        break
    else:
        i += 1
