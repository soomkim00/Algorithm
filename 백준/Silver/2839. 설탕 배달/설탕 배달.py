def solve():
    N = int(input())
    # 5로 나누어떨어지면 바로 출력
    if N % 5 == 0:
        print(N // 5)
        return
    a = N // 5
    while a >= 0:
        g = N - a * 5
        if g % 3 == 0:
            print(a + g // 3)
            return
        a -= 1
    print(-1)


if __name__ == "__main__":
    solve()
