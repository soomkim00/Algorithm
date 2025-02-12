T = int(input())

for tc in range(1, T + 1):
    t = int(input()[3:])
    num_name = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    num_list = list(input().split())
    num_sorted = []

    for name in num_name:
        for num in num_list:
            if num == name:
                num_sorted.append(num)
    print(f"#{tc}")
    print(*num_sorted)
