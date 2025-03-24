import sys

if __name__ == "__main__":
    N = int(input())
    a = set(list(map(int, input().split())))

    M = int(input())
    b = list(map(int, input().split()))
    for num in b:
        if num in a:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
