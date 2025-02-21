# 그 뭐시기냐 스위치 문제?랑 똑같은..

T = int(input())

for tc in range(1, T + 1):
    memory = list(map(int, input()))
    cnt = 0
    for i in range(len(memory)):
        if memory[i] == 1:
            for j in range(i, len(memory)):
                memory[j] = (memory[j] + 1) % 2
            cnt += 1

    print(f"#{tc} {cnt}")
