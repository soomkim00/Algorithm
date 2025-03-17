while True:
    n = input()

    if n == '0':
        break
    N = len(n)
    for i in range(N//2):
        if n[i] != n[N-1-i]:
            print('no')
            break
    else:
        print('yes')