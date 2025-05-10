import sys

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())

    data = {input().rstrip() for _ in range(N)}

    output = []
    for _ in range(M):
        name = input().rstrip()
        if name in data:
            output.append(name)

    output.sort()
    print(len(output))
    sys.stdout.write('\n'.join(output))


if __name__ == "__main__":
    solve()
