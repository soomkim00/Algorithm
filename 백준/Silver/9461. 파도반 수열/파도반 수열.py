import sys

input = sys.stdin.readline


def solve():
    tc = int(input())
    data = []

    for _ in range(tc):
        data.append(int(input()))

    result = [0, 1, 1, 1, 2, 2]  # 1번부터 사용, 0번 인덱스 버림

    max_val = max(data)
    if max_val >= 6:
        result.extend([0] * (max_val - 5))
        for i in range(6, max_val + 1):
            result[i] = result[i - 1] + result[i - 5]

    for num in data:
        print(result[num])


if __name__ == '__main__':
    solve()
