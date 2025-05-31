import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        data = dict()
        for _ in range(N):
            name, category = input().split()
            if category in data:
                data[category] += 1
            else:
                data[category] = 1
        data_arr = list(data.values())

        total = 0
        total += sum(data_arr)


if __name__ == "__main__":
    solve()
