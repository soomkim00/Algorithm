# 비교하는 대상에 0이 있으므로
# 초기화 대상을 다른 숫자로 설정
# 0~top까지만 출력하면 결과 스택 출력 가능

for tc in range(1, 11):
    N, password = input().split()
    N = int(N)
    password = list(password)

    my_stack = [99] * N
    top = -1

    for p in password:
        if top == -1:
            top += 1
            my_stack[top] = p
        elif my_stack[top] == p:
            my_stack[top] == 99
            top -= 1
        else:
            top += 1
            my_stack[top] = p

    result = "".join(my_stack[: top + 1])
    print(f"#{tc} {result}")
