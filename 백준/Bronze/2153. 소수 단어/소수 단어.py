def isprime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return "It is not a prime word."
    return "It is a prime word."


def convert(m):
    num = 0
    for i in m:
        if ord('a') <= ord(i) <= ord('z'):
            num += ord(i) - 96
        elif ord('A') <= ord(i) <= ord('Z'):
            num += ord(i) - 38
    return num


a = input()
print(isprime(convert(a)))
