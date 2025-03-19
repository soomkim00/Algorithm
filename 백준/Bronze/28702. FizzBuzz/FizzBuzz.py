arr = []
for _ in range(3):
    arr.append(input())

num = 0
for i in range(3):
    if arr[i].isdecimal():
        num = int(arr[i]) + (3 - i)
        break

if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0 and num % 5 != 0:
    print('Fizz')
elif num % 3 != 0 and num % 5 == 0:
    print('Buzz')
else:
    print(num)