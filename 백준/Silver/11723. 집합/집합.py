import sys

input = sys.stdin.readline


def solve():
    M = int(input())
    S = set()
    for _ in range(M):
        command = list(input().split())
        c = command[0]
        if len(command) == 1:
            if c == 'all':
                S = set(i for i in range(1, 21))
            elif c == 'empty':
                S = set()
        else:
            x = int(command[1])
            if c == 'add':
                S.add(x)
            elif c == 'remove' and x in S:
                S.remove(x)
            elif c == 'toggle':
                if x in S:
                    S.remove(x)
                else:
                    S.add(x)
            elif c == 'check':
                if x in S:
                    print(1)
                else:
                    print(0)


if __name__ == "__main__":
    solve()
