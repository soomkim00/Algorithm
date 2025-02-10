T = int(input())

for t in range(T):
    n = int(input())
    primes = [2, 3, 5, 7, 11]
    results = [0] * 5

    # 각 소수들을 접근하면서
    # 숫자가 소수로 나누어떨어지는동안
    # 나눠지는 수만큼 결과리스트를 증가
    for i in range(len(primes)):
        while n % primes[i] == 0:
            n = n // primes[i]
            results[i] += 1

    print(f'#{t + 1}', end=' ')
    for result in results:
        print(result, end=' ')
    print()
