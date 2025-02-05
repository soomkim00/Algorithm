T = int(input())


for _ in range(T):
    R, S = input().split()
    R = int(R)
    result = []

    for i in range(len(S)):
        result.extend(S[i] * R)

    for i in range(len(result)):
        print(result[i], end="")
    print()
