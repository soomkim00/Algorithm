T = int(input())
for tc in range(1, T + 1):
    word = list(input())
    check = 1

    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            check = 0
            break

    print(f"#{tc} {check}")
