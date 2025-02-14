left = ["(", "[", "{", "<"]
right = [")", "]", "}", ">"]

for tc in range(1, 11):
    n = int(input())
    bracket = list(input())

    my_stack = [0] * n
    top = -1
    check = 1

    for x in bracket:
        if x in left:
            top += 1
            my_stack[top] = x
        elif x in right:
            if top == -1:
                check = 0
                break
            top -= 1
            if left[right.index(x)] != my_stack[top + 1]:
                check = 0
                break
    if top != -1:
        check = 0

    print(f"#{tc} {check}")
