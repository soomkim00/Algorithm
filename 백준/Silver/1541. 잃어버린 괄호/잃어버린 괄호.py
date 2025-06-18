import sys
from collections import deque

input = sys.stdin.readline


def solve():
    data = input()

    temp = ''
    flag = 1  # 1:pos, 0:neg

    result = 0
    for d in data:
        if d not in ('-', '+'):
            temp += d
        else:
            if flag:
                if d == '-':
                    flag = 0
                result += int(temp)
            else:
                result -= int(temp)
            temp = ''

    if flag:
        result += int(temp)
    else:
        result -= int(temp)

    print(result)


if __name__ == '__main__':
    solve()
