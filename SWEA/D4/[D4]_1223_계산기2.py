T = 10

for tc in range(1, T + 1):
    N = int(input())
    case = list(input())
    p = ''
    stack = []
    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

    #  중위 -> 후위 표기법 변환
    for x in case:
        if x not in '(*/+-)':
            p += x
        elif x == ')':
            while stack[-1] != '(':
                p += stack.pop()
            stack.pop()
        else:
            if not stack or isp[stack[-1]] < icp[x]:
                stack.append(x)
            elif isp[stack[-1]] >= icp[x]:
                while stack and isp[stack[-1]] >= icp[x]:
                    p += stack.pop()
                stack.append(x)
    while stack:
        p += stack.pop()

    #  후위 표기법 수식의 스택을 사용한 연산
    for x in p:
        if x not in '(*/+-)':
            stack.append(int(x))
        else:
            rn, ln = stack.pop(), stack.pop()
            if x == '+':
                stack.append(ln + rn)
            elif x == '-':
                stack.append(ln - rn)
            elif x == '*':
                stack.append(ln * rn)
            elif x == '/':
                stack.append(ln / rn)
    print(f"#{tc} {stack.pop()}")
