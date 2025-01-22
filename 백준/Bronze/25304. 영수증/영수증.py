total = int(input())
num = int(input())
result = 0

for i in range(num):
    price, count = map(int, input().split())
    result += price * count

if result == total:
    print("Yes")
else:
    print("No")
