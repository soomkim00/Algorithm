T = int(input())

for tc in range(1, T + 1):
    n = int(input()) // 10
    tape = [0] * (n + 1)
    tape[1] = 1
    tape[2] = 3
    for i in range(3, n + 1):
        tape[i] = (tape[i - 2] * 2) + tape[i - 1]

    print(f'#{tc} {tape[n]}')
