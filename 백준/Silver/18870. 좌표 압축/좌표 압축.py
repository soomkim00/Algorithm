import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    data = list(map(int, input().split()))

    copy_data = data.copy()
    copy_data.sort()

    new_dict = dict()
    idx = 0
    for num in copy_data:
        if num not in new_dict:
            new_dict[num] = idx
            idx += 1

    for num in data:
        print(new_dict[num], end=' ')



if __name__ == '__main__':
    solve()
