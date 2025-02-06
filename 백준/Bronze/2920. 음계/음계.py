# 1~8 한번씩 등장
# 이어지는 두 숫자는 증가하거나, 감소하거나
# 총 7번 증가 == 모두 증가 == 'ascending'
# 총 7번 감소 == 모두 감소 == 'descending'
# 그 외 == 'mixed'


keys = list(map(int, input().split()))
check = 0

for i in range(len(keys) - 1):
    if keys[i] < keys[i + 1]:
        check += 1
    else:
        check -= 1

if check == 7:
    print("ascending")
elif check == -7:
    print("descending")
else:
    print("mixed")
