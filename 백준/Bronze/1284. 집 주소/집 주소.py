results = []

while True:
    num = input()
    if num == "0":
        break
    results.append(num)

for result in results:
    total = 0
    for i in result:
        if i == '1':
            total += 2
        elif i == '0':
            total += 4
        else:
            total += 3
    total += len(result) + 1
    print(total)
