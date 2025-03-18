N = int(input())

arr = [int(input()) for _ in range(N)]

arr.sort()

for num in arr:
    print(num)