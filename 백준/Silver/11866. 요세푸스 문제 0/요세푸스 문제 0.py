import sys

input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())

    visited = [0] * (N + 1)
    cnt = 0
    idx = 1
    order = 1
    result = []

    while cnt < N:
        if visited[idx]:
            idx = (idx + 1) % (N + 1)
            if idx == 0:
                idx = 1
        else:
            if order == K:
                visited[idx] = 1
                cnt += 1
                order = 1
                result.append(idx)
            else:
                idx = (idx + 1) % (N + 1)
                if idx == 0:
                    idx = 1
                order += 1
    sys.stdout.write('<')
    for i in range(N-1):
        print(result[i], end=', ')
    print(result[-1], end='>')


if __name__ == "__main__":
    solve()
