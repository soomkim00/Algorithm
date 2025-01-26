n = int(input())
stk1 = []
stk2 = []
count = 1
check = True

for _ in range(n):
    num = int(input())
    while count <= num:
        stk1.append(count)
        stk2.append('+')
        count += 1
    if stk1[-1] == num:
        stk1.pop()
        stk2.append('-')
    else:
        check = False

if check == False:
    print('NO')
else:
    for i in stk2:
        print(i)
