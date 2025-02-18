for tc in range(1, 11):
    n = int(input())
    cal_sen = input()
    stack = [0] * n
    top = -1
    result = ''

    for x in cal_sen:
        if x != '+':
            result += x
        elif top != -1:
            result += stack[top]
            stack[top] = x
        else:
            top += 1
            stack[top] = x

    while top > -1:
        result += stack[top]
        top -= 1

    for x in result:
        if x != '+':
            top += 1
            stack[top] = x
        else:
            top -= 1
            oper_r = stack[top + 1]
            top -= 1
            oper_l = stack[top + 1]
            stack[top] = int(oper_l) + int(oper_r)

    print(f'#{tc} {stack[top]}')
