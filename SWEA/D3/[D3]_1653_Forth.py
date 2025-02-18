def cal_forth(sen):
    stack = [0] * len(sen)
    top = -1

    for x in sen:
        #  끝났는데 스택에 남은게 하나가 아니면 오류,
        #  정상이면 top 값 return
        if x == '.':
            if top != 0:
                return 'error'
            else:
                return stack[top]
        
        #  숫자가 들어오면 push
        if x.isdecimal():
            top += 1
            stack[top] = int(x)
            continue

        #  연산자인데, 스택에 2개가 아니라면 식 오류
        if top <= 0:
            return 'error'

        #  연산자 두개 뽑아서 연산 후 스택에 저장
        oper_r = stack[top]
        top -= 1
        oper_l = stack[top]
        if x == '+':
            stack[top] = oper_l + oper_r
        elif x == '-':
            stack[top] = oper_l - oper_r
        elif x == '*':
            stack[top] = oper_l * oper_r
        elif x == '/':
            stack[top] = oper_l // oper_r


T = int(input())

for tc in range(1, T + 1):
    cal_sen = list(input().split())
    result = cal_forth(cal_sen)

    print(f"#{tc} {result}")
