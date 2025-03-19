import sys

if __name__ == "__main__":
    N = int(input())
    count = [0] * 10001
    for _ in range(N):
        count[int(sys.stdin.readline())] += 1

    for i in range(1, 10001):
        if count[i]:
            for _ in range(count[i]):
                print(i)
