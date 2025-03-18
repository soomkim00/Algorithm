import sys

if __name__ == "__main__":
    N = int(input())
    word = [[] for _ in range(51)]
    for _ in range(N):
        w = sys.stdin.readline().strip()
        word[len(w)].append(w)

    for i in range(51):
        if word[i]:
            word[i] = list(set(word[i]))
            word[i].sort()
            for w in word[i]:
                print(w)
