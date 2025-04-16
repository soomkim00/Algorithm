import sys

sys.stdin = open("input.txt", "r")


def solve():
    for tc in range(1, 11):
        N, start = map(int, input().split())
        data = list(map(int, input().split()))


        connect = [[] for _ in range(101)]
        visited = [0 for _ in range(101)]

        for i in range(0, N, 2):
            connect[data[i]].append(data[i + 1])

        visited[start] = 1
        now = [start]
        next = []
        while True:
            for n in now:
                for c in connect[n]:
                    if visited[c] == 0:
                        next.append(c)
                        visited[c] = 1
            if not next:
                break

            now = []
            while next:
                now.append(next.pop())

        print(f"#{tc} {max(now)}")


if __name__ == "__main__":
    solve()

"""
#1 17
#2 96
#3 49
#4 39
#5 49
#6 1
#7 28
#8 45
#9 59
#10 64
"""
