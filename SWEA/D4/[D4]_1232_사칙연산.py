def cal(n: int):
    # 자식이 없다? == 숫자다. 본인 return
    if not(left[n]) and not(right[n]):
        return float(nord[n])
    # 숫자가 아니다 == 연산자다
    if nord[n] == '+':
        return float(cal(left[n]) + cal(right[n]))
    elif nord[n] == '-':
        return float(cal(left[n]) - cal(right[n]))
    elif nord[n] == '*':
        return float(cal(left[n]) * cal(right[n]))
    elif nord[n] == '/':
        return float(cal(left[n]) / cal(right[n]))


for t in range(1, 11):
    N = int(input())
    nord = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    # 입력 값의 길이에 따라서 연산자와 피연산자 구분
    for _ in range(N):
        arr = list(input().split())
        nord[int(arr[0])] = arr[1]
        if len(arr) > 2:
            left[int(arr[0])] = int(arr[2])
            right[int(arr[0])] = int(arr[3])

    print(f'#{t} {int(cal(1))}')
