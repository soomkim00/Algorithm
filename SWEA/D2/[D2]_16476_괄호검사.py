# 왼쪽 괄호면 push
# 오른쪽 괄호면
# 1 스택 비었으면 비정상
# 2 스택의 top과 쌍을 이루지 않으면 비정상
# 3 둘 다 아니면 하나 pop
# 순환 후 스택 남아있으면 비정상

T = int(input())
left = ["{", "("]
right = ["}", ")"]

for tc in range(1, T + 1):
    code = list(input())

    my_stack = [0] * len(code)
    top = -1
    check = 1

    for c in code:
        if c in left:
            top += 1
            my_stack[top] = c
        elif c in right:
            if top == -1:
                check = 0
                break
            elif my_stack[top] != left[right.index(c)]:
                check = 0
                break
            else:
                top -= 1
    if top != -1:
        check = 0

    print(f"#{tc} {check}")
