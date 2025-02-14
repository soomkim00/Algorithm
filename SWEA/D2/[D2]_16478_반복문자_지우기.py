# 스택 비어있으면 하나 삽입
# 비어있지 않다면 top과 넣으려는 값 비교
# 같으면 top 0으로 초기화
# 전부 동작 후 문자의 개수를 출력

T = int(input())

for tc in range(1, T + 1):
    word = list(input())
    my_stack = [0] * len(word)
    top = -1
    for w in word:
        if top == -1:
            top += 1
            my_stack[top] = w
        elif my_stack[top] == w:
            my_stack[top] = 0
            top -= 1
        else:
            top += 1
            my_stack[top] = w

    count = 0
    for s in my_stack:
        if s == 0:
            break
        else:
            count += 1

    print(f"#{tc} {count}")
