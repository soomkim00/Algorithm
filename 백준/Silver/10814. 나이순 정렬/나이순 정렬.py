N = int(input())
order_list = [[] for _ in range(201)]
for _ in range(N):
    age, name = list(input().split())
    order_list[int(age)].append([age, name])

for i in range(201):
    for profile in order_list[i]:
        print(*profile)
