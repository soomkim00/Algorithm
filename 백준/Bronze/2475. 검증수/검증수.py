num = list(map(int, input().split()))
check = 0
for n in num:
    check += n ** 2
print(check % 10)
