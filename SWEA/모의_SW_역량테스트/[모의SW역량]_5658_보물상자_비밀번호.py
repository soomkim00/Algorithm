import sys

sys.stdin = open("input.txt", "r")

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T + 1):
        N, K = map(int, input().split())
        n = input() * 2
        r = []
        for i in range(N // 4):
            for j in range(i, i + N, N // 4):
                r.append(int(n[j:j + N // 4], 16))
        r = sorted(list(set(r)), reverse=True)
        print(f"#{tc} {r[K - 1]}")
