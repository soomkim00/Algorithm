import sys
from collections import deque

input = sys.stdin.readline


def solve():
    M, N, H = map(int, input().split())
    data = []
    for _ in range(H):
        layer = [list(map(int, input().split())) for _ in range(N)]
        data.append(layer)

    tomatos = set()
    count = 0
    for d in range(H):
        for r in range(N):
            for c in range(M):
                if 

if __name__ == '__main__':
    solve()
