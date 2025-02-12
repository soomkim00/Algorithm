T = int(input())

for tc in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())
    max_count = 0

    for a in str1:
        count = 0
        for b in str2:
            if a == b:
                count += 1
        if max_count < count:
            max_count = count

    print(f"#{tc} {max_count}")
