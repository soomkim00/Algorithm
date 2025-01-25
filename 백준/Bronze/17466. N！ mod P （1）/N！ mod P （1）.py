def factorial_mod(n, p):
    num = 1
    for i in range(2, n+1):
        num = (num * i) % p
    return num % p


N, P = map(int, input().split())
print(factorial_mod(N, P))
