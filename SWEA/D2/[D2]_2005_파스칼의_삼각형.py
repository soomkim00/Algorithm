# 양 끝 값은 무조건 1
# 그외의 값은 이전 줄 리스트의 해당 인덱스 + 해당 인덱스-1
# 완성된 리스트 출력 후 해당 리스트정보와 함께 다음 함수 호출

def print_pascal(i, n, arr):
    result = []
    for j in range(i):
        if j == 0 or j == i - 1:
            result.append(1)
        else:
            result.append(arr[j - 1] + arr[j])
    print(*result)
    if i == n:
        return
    print_pascal(i + 1, n, result)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print(f"#{tc}")
    print_pascal(1, N, [1])
