import sys

if __name__ == "__main__":
    N = int(input())
    total = 1
    for i in range(2, N + 1):
        total *= i
    cnt = 0
    while True:
        if total % 10 != 0:
            break
        else:
            cnt += 1
            total //= 10
    print(cnt)
