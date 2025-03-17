T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    apt = [[0] * n for _ in range(k+1)]
    for i in range(n):
        apt[0][i] = i+1
    for i in range(k+1):
        apt[i][0] = 1

    for r in range(1, k+1):
        for c in range(1, n):
            apt[r][c] = apt[r-1][c] + apt[r][c-1]

    print(apt[k][n-1])
