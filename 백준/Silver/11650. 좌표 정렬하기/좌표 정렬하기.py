N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]
p.sort(key=lambda x: x[1])
p.sort()
for n in p:
    print(*n)
