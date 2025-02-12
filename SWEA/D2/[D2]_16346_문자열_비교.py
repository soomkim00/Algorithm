def is_match(s1, s2):
    N, M = len(s1), len(s2)
    for i in range(M - N + 1):
        for j in range(N):
            if s2[i + j] != s1[j]:
                break
        else:
            return 1
    return 0


T = int(input())

for tc in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())
    result = is_match(str1, str2)

    print(f"#{tc} {result}")
