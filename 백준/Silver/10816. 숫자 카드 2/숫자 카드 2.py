import sys


def solve():
    N = sys.stdin.readline()
    a = list(map(int, sys.stdin.readline().split()))
    M = sys.stdin.readline()
    b = list(map(int, sys.stdin.readline().split()))

    cnt = {}
    for c in a:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1

    for d in b:
        sys.stdout.write(str(cnt.get(d, 0))+' ')


if __name__ == "__main__":
    solve()
